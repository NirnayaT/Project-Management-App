from Database.database import User, session
from repository import AbstractRepositoryForUser
from pydantic import EmailStr
from Users.auth.jwt_handler import signJWT
from Users.tokens.hash import Hash


class UserRepository(AbstractRepositoryForUser):

    def add(self, new_username: str, new_email: EmailStr, password: str):
        new_user_object = User(
            username=new_username,
            email=new_email,
            password_hash=Hash.pass_hash(password),
        )
        session.add(new_user_object)
        session.commit()
        session.refresh(new_user_object)
        return signJWT(new_user_object.email)
