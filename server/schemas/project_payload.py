from typing import Optional
from pydantic import BaseModel
from datetime import date


class CreateProjectPayload(BaseModel):
    """
    Defines a Pydantic model for the payload of a request to create a new project.
    """
        
    project_name: str
    project_description: str
    start_date: date
    end_date: Optional[date] = None


class RemoveProjectPayload(BaseModel):
    """
    Defines a Pydantic model for the payload of a request to remove a project.

    """
        
    project_id: int


class UpdateProjectPayload(BaseModel):
    """
    Defines a Pydantic model for the payload of a request to update an existing project.

    """
        
    project_id: int
    new_project_name: Optional[str]=None
    new_project_description: Optional[str]=None
    start_date: Optional[date]=None
    end_date: Optional[date] = None
    
