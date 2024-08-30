from typing import Optional
from pydantic import BaseModel, EmailStr, model_validator
import re


class UserCreatePayload(BaseModel):
    """
    Represents the payload for creating a new user.

    """
        
    username: str
    email: EmailStr
    password: str


class UserLoginPayload(BaseModel):
    """
    Represents the payload for authenticating a user.
    
    """
        
    email: EmailStr
    password: str


class PasswordChangePayload(BaseModel):
    """
    Represents the payload for changing a user's password.

    """
        
    old_password: str
    new_password: str
    confirm_new_password: str

    
class ResetPasswordPayload(BaseModel):
    """
    Represents the payload for resetting a user's password.
    
    """
        
    token: str
    new_password: str
    confirm_password: str

class DetailsChangePayload(BaseModel):
    """
    Represents the payload for changing a user's details, such as username and email.
    
    """
        
    username: Optional[str] = None
    email : Optional[EmailStr] = None

