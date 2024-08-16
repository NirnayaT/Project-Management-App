from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user_payload import UserCreatePayload
from models.users import User
from config.database import *
from sqlalchemy.exc import IntegrityError
from response.user_responses import UserResponse
from service.user_services import create_user, get_user_details
from utils.auth.jwt_handler import (
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_current_active_user,
    get_current_user,
    get_db,
)
from sqlalchemy.orm import Session
from decouple import config

ACCESS_TOKEN_EXPIRE_MINUTES = int(config("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(config("REFRESH_TOKEN_EXPIRE_DAYS"))

router = APIRouter(
    prefix="/user",
    tags=["User Management"]
)


@router.post("/register")
def register_user(create_user_data: UserCreatePayload):
    try:
        return create_user(create_user_data)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Username or email already registered"
        )


@router.post("/login")
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
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
        "user":{
            "id":user.id,
            "username": user.username,
            "email": user.email
        }
    }


@router.get("/details", response_model=list[UserResponse])
def get_user(current_user: User = Depends(get_current_user)):
    return get_user_details()


@router.get("", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
