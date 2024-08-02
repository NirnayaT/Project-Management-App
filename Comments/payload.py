from pydantic import BaseModel


class CreateCommentPayload(BaseModel):
    task_id: int
    comment: str
    user_id: int


class RemoveCommentPayload(BaseModel):
    task_id: int
    comment_id: int


class UpdateCommentPayload(BaseModel):
    task_id: int
    comment_id: int
    new_comment: str
