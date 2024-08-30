from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class CreateProjectResponse(BaseModel):
    """
    Represents the response data for creating a new project.
    
    Attributes:
        id (int): The unique identifier for the project.
        name (str): The name of the project.
        description (str): The description of the project.
        created_at (datetime): The date and time the project was created.
        start_date (date): The start date of the project.
        end_date (Optional[date]): The optional end date of the project.
        owner_id (int): The identifier of the user who owns the project.
    """
        
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int



class RemoveProjectResponse(BaseModel):
    """
    Represents the response data for removing a project.
    
    Attributes:
        id (int): The unique identifier for the project.
        name (str): The name of the project.
        description (str): The description of the project.
        created_at (datetime): The date and time the project was created.
        start_date (date): The start date of the project.
        end_date (Optional[date]): The optional end date of the project.
        owner_id (int): The identifier of the user who owns the project.
    """
        
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int


class UpdateProjectResponse(BaseModel):
    """
    Represents the response data for updating a project.
    
    Attributes:
        id (int): The unique identifier for the project.
        name (str): The name of the project.
        description (str): The description of the project.
        created_at (datetime): The date and time the project was created.
        start_date (date): The start date of the project.
        end_date (Optional[date]): The optional end date of the project.
        owner_id (int): The identifier of the user who owns the project.
        user_name (Optional[str]): The optional name of the user who updated the project.
    """
        
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int
    user_name: Optional[str] = None  

class ProjectResponse(BaseModel):
    """
    Represents the response data for a project.
    
    Attributes:
        id (int): The unique identifier for the project.
        name (str): The name of the project.
        description (str): The description of the project.
        created_at (datetime): The date and time the project was created.
        start_date (date): The start date of the project.
        end_date (Optional[date]): The optional end date of the project.
        owner_id (int): The identifier of the user who owns the project.
    """
        
    id: int
    name: str
    description: str
    created_at: datetime
    start_date: date
    end_date: Optional[date]=None
    owner_id: int