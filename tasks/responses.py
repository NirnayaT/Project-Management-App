from pydantic import BaseModel
from datetime import datetime


class CreateTaskResponse(BaseModel):
    id: int
    task: str
    is_complete: str
    created_on: datetime
    project_name: str

class RemoveTaskResponse(BaseModel):
    id: int
    task: str
    is_complete: str
    created_on: datetime
    project_name: str
    
class UpdateTaskResponse(BaseModel):
    id: int
    new_task: str
    is_complete: str
    created_on: datetime
    project_name: str
    
class TaskResponse(BaseModel):
    id: int
    task: str
    is_complete: str
    created_on: datetime
    project_name: str

