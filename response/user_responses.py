from pydantic import BaseModel, EmailStr


class UserDetailResponse(BaseModel):
    username: str
    email: EmailStr
    
class UserResponse(BaseModel):
    username: str
    email: EmailStr
    id : int