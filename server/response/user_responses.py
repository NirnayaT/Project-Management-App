from pydantic import BaseModel, EmailStr


class UsersDetailResponse(BaseModel):
    """
    Represents a user's details, including their username, email, unique identifier, and active status.
    """

    username: str
    email: EmailStr
    id: int
    is_active: bool
    is_verified: bool


class UserResponse(BaseModel):
    """
    Represents a user's details, including their username, email, unique identifier, and active status.
    """

    username: str
    email: EmailStr
    id: int
    is_active: bool
    is_verified: bool


class CombinedResponse(UserResponse):
    """
    Represents a combined response, including the user's 
    details as well as additional content.
    """

    content: str = None
