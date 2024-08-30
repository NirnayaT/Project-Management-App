from datetime import timedelta
from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    UploadFile,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_mail import FastMail
from pydantic import EmailStr
from schemas.user_payload import (
    DetailsChangePayload,
    PasswordChangePayload,
    ResetPasswordPayload,
    UserCreatePayload
)
from models.users import User
from config.database import *
from sqlalchemy.exc import IntegrityError
from response.user_responses import CombinedResponse, UserResponse, UsersDetailResponse
from response.image_response import ImageResponse
from config.config import Config
from utils.email_utils import send_reset_email, send_verification_email
from utils.tokens.reset_password import (
    create_reset_token,
    create_verification_token,
    verify_reset_token,
)
from utils.tokens.hash import Hash
from service.image_service import (
    get_user_by_email,
    image_to_base64,
    save_image,
    update_image,
)
from service.user_services import change_details, create_user, get_users
from utils.tokens.jwt_handler import (
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_current_active_user,
    get_current_user,
)
import re
import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = Config.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = Config.REFRESH_TOKEN_EXPIRE_DAYS
SECRET_KEY = Config.SECRET_KEY
ALGORITHM = Config.ALGORITHM

router = APIRouter(prefix="/user", tags=["User Management"])


@router.post("/register")
async def register_user(create_user_data: UserCreatePayload):
    try:
        new_user = create_user(create_user_data)
        if not new_user:
            raise HTTPException(status_code=500, detail="User creation failed")
        if not new_user.email:
            raise HTTPException(
                status_code=500, detail="Email missing from user object"
            )

        token = create_verification_token(new_user.email)
        verification_link = (
            f"http://localhost:8000/api/v1/user/verify-email?token={token}"
        )
        try:
            await send_verification_email(
                email=new_user.email, verification_link=verification_link
            )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to send verification email: {e}"
            )
        return {
            "msg": "Registration successful. Please check your email for verification."
        }
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Username or email already registered"
        )


@router.get("/verify-email")
def verify_email(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        email = payload.get("email")

        user = session.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.is_verified = True
        session.add(user)
        session.commit()
        return {"msg": "Email verification successful"}

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Verification token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid verification token")


@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    refresh_token = create_refresh_token(data={"sub": user.email})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": {"id": user.id, "username": user.username, "email": user.email},
    }


@router.get("/all", response_model=list[UsersDetailResponse])
def get_all_users(current_user: User = Depends(get_current_user)):
    return get_users()


@router.get("/details", response_model=CombinedResponse)
async def read_user_detail(current_user: User = Depends(get_current_active_user)):
    current_user.content = image_to_base64(current_user)
    return current_user


@router.post("/upload-image", response_model=ImageResponse)
async def upload_image(
    file: UploadFile = File(...),  # multipart data
    current_user: User = Depends(get_current_user),
):

    user = session.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    image = save_image(file, current_user.id)
    return image


@router.put("/image/update")
async def image_update(
    file: UploadFile = File(...), current_user: User = Depends(get_current_user)
):
    user = session.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    image = update_image(file, current_user.id)
    return image


@router.patch("/change-password")
def change_password(
    request: PasswordChangePayload,
    current_user: User = Depends(get_current_user),
):
    if not Hash.verify_password(request.old_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect old password.")

    if request.new_password != request.confirm_new_password:
        raise HTTPException(
            status_code=400, detail="New password and confirm password do not match."
        )

    current_user.password_hash = Hash.password_hash(request.new_password)
    session.add(current_user)
    session.commit()

    return {"msg": "Password has been reset successfully."}

@router.patch("/change-details")
def change_user_details(
    payload: DetailsChangePayload,
    current_user: User = Depends(get_current_user),
):
    return change_details(email=payload.email, username=payload.username, user_id=current_user.id)


@router.post("/reset-password")
async def reset_password(reset_data: ResetPasswordPayload):
    email = verify_reset_token(reset_data.token)

    user = get_user_by_email(email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_password = reset_data.new_password
    confirm_password = reset_data.confirm_password

    if new_password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    password_regex = (
        r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>]).{8,}$"
    )

    if not re.match(password_regex, new_password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.",
        )
    new_hashed_password = Hash.password_hash(new_password)
    user.password_hash = new_hashed_password
    session.commit()
    return {"msg": "Password reset successful"}


@router.post("/request-password-reset")
async def request_password_reset(email: EmailStr, user=Depends(get_user_by_email)):
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    reset_token = create_reset_token(user.email)
    reset_link = f"http://localhost:5173/reset-password?token={reset_token}"

    try:
        await send_reset_email(email=user.email, reset_link=reset_link)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")

    return {"msg": "Password reset email sent"}
