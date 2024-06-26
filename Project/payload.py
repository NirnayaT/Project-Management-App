from pydantic import BaseModel


class CreateProjectPayload(BaseModel):
    project_name: str
    project_description: str
    owner_id: int

class RemoveProjectPayload(BaseModel):
    project_id: int
    
class UpdateProjectPayload(BaseModel):
    project_id : int
    new_project_name : str
    new_project_description : str

