from fastapi import HTTPException
from pydantic import EmailStr
from models.users import User
from schemas.user_payload import UserCreatePayload
from repository.user_repository import UserRepository
from config.database import *

# from Users.responses import UserDetailResponse
import re

from utils.tokens.hash import Hash

user_instance = UserRepository()


def create_user(user_data: UserCreatePayload):
    password_regex = (
        r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>]).{8,}$"
    )

    if not re.match(password_regex, user_data.password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long.",
        )
    hashed_password = Hash.password_hash(user_data.password)

    new_user = user_instance.add(
        new_username=user_data.username,
        new_email=user_data.email,
        password=hashed_password,
        is_active=True,
        is_verified=False,
    )
    if new_user is None:
        raise HTTPException(status_code=500, detail="User already exists")

    return new_user


def get_user_id(user_email: str):
    user = session.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="OwnerID not found")
    return user.id


def get_users():
    user = session.query(User).all()
    if not user:
        raise HTTPException(status_code=404, detail="No User found!")
    return user


def change_details(username: str, email: EmailStr, user_id: int):
    changed_details = user_instance.change_details(username=username, email=email, user_id=user_id)
    if not changed_details:
        raise HTTPException(status_code=404, detail="Details not changed.")
    if changed_details == username:
        return {"Username changed successfully": changed_details}
    if changed_details == email:
        return {"Email changed successfully": changed_details}
    if changed_details.username == username and changed_details.email == email:
        return {"Username and Email changed successfully": f"{changed_details.username}, {changed_details.email}"}