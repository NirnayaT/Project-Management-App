from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class CreateProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime



class RemoveProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime



class UpdateProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    

