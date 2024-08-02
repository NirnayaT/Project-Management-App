from pydantic import BaseModel


class CreateTaskPayload(BaseModel):
    project_id: int
    task: str
    is_complete: str


class RemoveTaskPayload(BaseModel):
    project_id: int
    task_id: int


class UpdateTaskPayload(BaseModel):
    project_id: int
    task_id: int
    new_task: str
    is_complete: str
