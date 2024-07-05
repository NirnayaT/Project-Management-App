from fastapi import APIRouter, HTTPException
from Users.payload import UserCreatePayload, UserLoginPayload
from Database.database import User
from Database.database import *
from sqlalchemy.exc import IntegrityError
from Users.services import create_user
from Users.tokens.hash import Hash
from Users.auth.jwt_handler import signJWT

router = APIRouter()


@router.post("/register")
def register_user(create_user_data: UserCreatePayload):
    try:
        return create_user(create_user_data)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Username or email already registered"
        )

@router.post("/login")
def login_user(get_user_data: UserLoginPayload):
    user = session.query(User).filter(User.email == get_user_data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not Found")
    verification = Hash.verify_pass(get_user_data.password, user.password_hash)
    if verification == False:
        raise HTTPException(status_code=401, detail="Incorrect password")
    elif verification == True:
        return signJWT(get_user_data.email)
    
