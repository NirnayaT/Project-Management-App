from pydantic import BaseModel


class CreateTaskPayload(BaseModel):
    task: str


class RemoveTaskPayload(BaseModel):
    task_id: int
