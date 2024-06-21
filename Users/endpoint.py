from fastapi import APIRouter,HTTPException
from Users.payload import UserCreatePayload, UserLoginPayload
from Database.database import User
from Database.database import *
from sqlalchemy.exc import IntegrityError
from hash import Hash
import datetime
router = APIRouter()


@router.post("/register")
def register_user(create_user_data: UserCreatePayload):
    try:
        new_user=User(
            username = create_user_data.username,
            email = create_user_data.email,
            password_hash = Hash.pass_hash(create_user_data.password)
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already registered")

