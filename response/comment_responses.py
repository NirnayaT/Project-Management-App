from pydantic import BaseModel
from datetime import datetime


class CreateCommentResponse(BaseModel):
    id: int
    comment: str
    created_on: datetime
    task_name: str


class RemoveCommentResponse(BaseModel):
    id: int
    comment: str
    created_on: datetime
    task_name: str


class UpdateCommentResponse(BaseModel):
    id: int
    new_comment: str
    created_on: datetime
    task_name: str


class CommentResponse(BaseModel):
    id: int
    comment: str
    created_on: datetime
    task_name: str
