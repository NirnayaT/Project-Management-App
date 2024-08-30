from typing import Optional
from pydantic import BaseModel
from datetime import date


class CreateProjectPayload(BaseModel):
    project_name: str
    project_description: str
    start_date: date
    end_date: Optional[date] = None


class RemoveProjectPayload(BaseModel):
    project_id: int


class UpdateProjectPayload(BaseModel):
    project_id: int
    new_project_name: Optional[str]=None
    new_project_description: Optional[str]=None
    start_date: Optional[date]=None
    end_date: Optional[date] = None
    
