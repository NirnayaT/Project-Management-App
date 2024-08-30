from typing import Optional
from pydantic import BaseModel
from datetime import date


class CreateTaskPayload(BaseModel):
    """
    Represents the payload for creating a new task.
    """
        
    project_id: int
    task: str
    status: str
    priority: str
    assignee_id: int
    due_date: date


class RemoveTaskPayload(BaseModel):
    """
    Represents the payload for removing a task.
    
    """
        
    project_id: int
    task_id: int


class UpdateTaskPayload(BaseModel):
    """
    Represents the payload for updating an existing task.

    """
        
    project_id: Optional[int]=None
    task_id: Optional[int]=None
    new_task: Optional[str]=None
    status: Optional[str]=None
    priority: Optional[str]=None
    assignee_id: Optional[int]=None
    due_date: Optional[date]=None
