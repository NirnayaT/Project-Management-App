from typing import Optional
from pydantic import BaseModel, EmailStr, model_validator
import re


class UserCreatePayload(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLoginPayload(BaseModel):
    email: EmailStr
    password: str


class PasswordChangePayload(BaseModel):
    old_password: str
    new_password: str
    confirm_new_password: str

    
class ResetPasswordPayload(BaseModel):
    token: str
    new_password: str
    confirm_password: str

class DetailsChangePayload(BaseModel):
    username: Optional[str] = None
    email : Optional[EmailStr] = None

