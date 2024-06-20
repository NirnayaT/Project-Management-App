from pydantic import BaseModel
from datetime import datetime

class CreateTaskResponse(BaseModel):
    id: int
    task: str
    is_complete: bool
    created_on: datetime

class RemoveTaskResponse(BaseModel):
    id: int
    task: str
    is_complete: bool
    created_on: datetime