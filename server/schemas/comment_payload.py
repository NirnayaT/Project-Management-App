from pydantic import BaseModel


class CreateCommentPayload(BaseModel):
    """
    Represents the payload for creating a new comment on a task.
    """
        
    task_id: int
    comment: str


class RemoveCommentPayload(BaseModel):
    """
    Represents the payload for removing a comment from a task.
    """
        
    task_id: int
    comment_id: int


class UpdateCommentPayload(BaseModel):
    """
    Represents the payload for updating an existing comment on a task.
    """
        
    task_id: int
    comment_id: int
    new_comment: str
