from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from decouple import config
from sqlalchemy.orm import Session
import time
from models.users import User
from config.database import session
from utils.tokens.hash import Hash


SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(config("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(config("REFRESH_TOKEN_EXPIRE_DAYS"))


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


<<<<<<< HEAD:server/utils/tokens/jwt_handler.py
=======
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
>>>>>>> 727e267977f9f425154a0ab509e9f07372a8e2bb:utils/auth/jwt_handler.py
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/user/login")




app = FastAPI()



def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def authenticate_user(email: str, password: str):
    user = get_user(session, email)
    if not user or not Hash.verify_password(password, user.password_hash):
        return False

    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"expiry": expire.timestamp()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    payload = data.copy()
    expire = time.time() + 60 * 60 * 24 * REFRESH_TOKEN_EXPIRE_DAYS
    payload.update(
        {
            "expiry": expire,
        }
    )

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


async def get_current_user(
     token: str = Depends(oauth2_scheme)
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data = TokenData(email=username)
    except JWTError:
        raise credential_exception

    user = get_user(session, email=token_data.email)
    if user is None:
        raise credential_exception

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


