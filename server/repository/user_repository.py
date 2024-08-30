from pydantic import EmailStr
from config.database import session
from repository.repository import AbstractRepositoryForUser
from models.users import User


class UserRepository(AbstractRepositoryForUser):

    def add(
        self,
        new_username: str,
        new_email: str,
        password: str,
        is_active: bool,
        is_verified: bool,
    ):
        try:
            new_user_object = User(
                username=new_username,
                email=new_email,
                password_hash=password,
                is_active=is_active,
                is_verified=is_verified,
            )
            session.add(new_user_object)
            session.commit()
            session.refresh(new_user_object)
            print(f"User created: {new_user_object}")  # Debugging print
            return new_user_object
        except Exception as e:
            session.rollback()
            print(f"Error adding user: {e}")
            return None
        
    def change_details(
          self,
          username: str,
          email: EmailStr,  
          user_id: int,
        ):
        change_details = session.query(User).filter(User.id == user_id).first()
        if change_details:
            if username is not None:
                change_details.username = username
            if email is not None:
                change_details.email = email
            session.commit()
        if username and email:
            return change_details
        if username:
            return change_details.username
        if email:
            return change_details.email
        
                
