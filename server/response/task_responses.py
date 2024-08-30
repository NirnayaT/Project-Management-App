from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime
from response.project_responses import ProjectResponse


class CreateTaskResponse(BaseModel):
    id: int
    task: str
    status: str
    created_on: datetime
    # project_name: str
    priority: str
    assignee_id: int
    due_date: date
    project_id:int

class RemoveTaskResponse(BaseModel):
    id: int
    task: str
    status: str
    created_on: datetime
    priority: str
    assignee_id: int
    due_date: date
    project_id:int

class UpdateTaskResponse(BaseModel):
    id: int
    new_task: str
    status: str
    created_on: datetime
    project_name: str
    priority: str
    assignee_id: int
    due_date: date
    project_id:int

class UserResource(BaseModel):
    username: str

class TaskResponse(BaseModel):
    id: int
    task: str
    status: str
    created_on: datetime
    priority: str
    assignee: Optional[UserResource] = None
    due_date: date
    # project: Optional[ProjectResponse] = None
