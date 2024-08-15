from config.database import session
from repository.repository import AbstractRepositoryForUser
from pydantic import EmailStr
from utils.tokens.hash import Hash
from models.users import User


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
        
