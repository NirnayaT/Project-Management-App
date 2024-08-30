from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime
from response.project_responses import ProjectResponse


class CreateTaskResponse(BaseModel):
    """
    Represents the response data for creating a new task.
    
    Attributes:
        id (int): The unique identifier for the task.
        task (str): The title or description of the task.
        status (str): The current status of the task.
        created_on (datetime): The date and time the task was created.
        priority (str): The priority level of the task.
        assignee_id (int): The ID of the user assigned to the task.
        due_date (date): The date the task is due.
        project_id (int): The ID of the project the task belongs to.
    """
        
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
    """
    Represents the response data for removing a task.
    
    Attributes:
        id (int): The unique identifier for the task.
        task (str): The title or description of the task.
        status (str): The current status of the task.
        created_on (datetime): The date and time the task was created.
        priority (str): The priority level of the task.
        assignee_id (int): The ID of the user assigned to the task.
        due_date (date): The date the task is due.
        project_id (int): The ID of the project the task belongs to.
    """
        
    id: int
    task: str
    status: str
    created_on: datetime
    priority: str
    assignee_id: int
    due_date: date
    project_id:int

class UpdateTaskResponse(BaseModel):
    """
    Represents the response data for updating an existing task.
    
    Attributes:
        id (int): The unique identifier for the task.
        new_task (str): The new title or description of the task.
        status (str): The current status of the task.
        created_on (datetime): The date and time the task was created.
        project_name (str): The name of the project the task belongs to.
        priority (str): The priority level of the task.
        assignee_id (int): The ID of the user assigned to the task.
        due_date (date): The date the task is due.
        project_id (int): The ID of the project the task belongs to.
    """
        
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
    """
    Represents a user resource, containing the username.
    """
        
    username: str

class TaskResponse(BaseModel):
    """
    Represents the response data for a task.
    
    Attributes:
        id (int): The unique identifier for the task.
        task (str): The title or description of the task.
        status (str): The current status of the task.
        created_on (datetime): The date and time the task was created.
        priority (str): The priority level of the task.
        assignee (Optional[UserResource]): The user assigned to the task.
        due_date (date): The date the task is due.
    """
        
    id: int
    task: str
    status: str
    created_on: datetime
    priority: str
    assignee: Optional[UserResource] = None
    due_date: date
    # project: Optional[ProjectResponse] = None
