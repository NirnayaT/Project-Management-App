from pydantic import BaseModel, EmailStr


class UserCreatePayload(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLoginPayload(BaseModel):
    email: EmailStr
    password: str
