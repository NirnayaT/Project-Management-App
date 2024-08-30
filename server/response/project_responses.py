from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class CreateProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int



class RemoveProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int


class UpdateProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int
    user_name: Optional[str] = None  

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int