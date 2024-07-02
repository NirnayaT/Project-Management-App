from pydantic import BaseModel


class ShowTaskPayload(BaseModel):
    project_id: int


class CreateTaskPayload(BaseModel):
    project_id: int
    task: str
    

class RemoveTaskPayload(BaseModel):
    project_id: int
    task_id: int


class UpdateTaskPayload(BaseModel):
    project_id: int
    task_id: int
    new_task: str