from typing import Optional
from pydantic import BaseModel
from datetime import date


class CreateTaskPayload(BaseModel):
    """
    Represents the payload for creating a new task.
    """

    task: str
    status: str
    priority: str
    assignee_id: int
    due_date: date


class RemoveTaskPayload(BaseModel):
    """
    Represents the payload for removing a task.

    """

    task_id: int


class UpdateTaskPayload(BaseModel):
    """
    Represents the payload for updating an existing task.

    """

    task_id: Optional[int] = None
    new_task: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assignee_id: Optional[int] = None
    due_date: Optional[date] = None
    
class ShowTaskPayload(BaseModel):
    """
    Represents the payload for showing a task.
    """
    project_id: int
        
