from pydantic import BaseModel, EmailStr


class UsersDetailResponse(BaseModel):
    username: str
    email: EmailStr
    id: int
    is_active: bool


class UserResponse(BaseModel):
    username: str
    email: EmailStr
    id: int
    is_active: bool

class CombinedResponse(UserResponse):
    content: str = None
