from fastapi import HTTPException
from models.users import User
from schemas.user_payload import UserCreatePayload
from repository.user_repository import UserRepository
from config.database import *
# from Users.responses import UserDetailResponse


user_instance = UserRepository()


def create_user(user_data: UserCreatePayload):
    new_user = user_instance.add(
        user_data.username, user_data.email, user_data.password
    )
    return{"User_Registered": user_data.username}


def get_user_name(owner_id: int):
    user = session.query(User).filter(User.id == owner_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.username


def get_user_id(user_email: str):
    user = session.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="OwnerID not found")
    return user.id


def get_user_details():
    user = session.query(User).all()
    if not user:
        raise HTTPException(status_code=404, detail="No User found!")
    # return UserDetailResponse(username=user.username, email=user.email)
    return user
