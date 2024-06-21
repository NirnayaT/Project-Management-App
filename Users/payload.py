from pydantic import BaseModel

class UserCreatePayload(BaseModel):
    username: str
    email: str
    password: str

class UserLoginPayload(BaseModel):
    username: str
    password: str