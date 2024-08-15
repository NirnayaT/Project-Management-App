from pydantic import BaseModel
from datetime import date


class CreateTaskPayload(BaseModel):
    project_id: int
    task: str
    status: str
    priority: str
    assignee_id: int
    due_date: date


class RemoveTaskPayload(BaseModel):
    project_id: int
    task_id: int


class UpdateTaskPayload(BaseModel):
    project_id: int
    task_id: int
    new_task: str
    status: str
    priority: str
    assignee_id: int
    due_date: date
