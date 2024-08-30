from pydantic import BaseModel
from datetime import datetime


class CreateCommentResponse(BaseModel):
    """
    Represents the response data for creating a new comment.
    
    Attributes:
        id (int): The unique identifier for the comment.
        comment (str): The text content of the comment.
        created_on (datetime): The timestamp when the comment was created.
        task_name (str): The name of the task associated with the comment.
    """
        
    id: int
    comment: str
    created_on: datetime
    task_name: str


class RemoveCommentResponse(BaseModel):
    """
    Represents the response data for removing a comment.
    
    Attributes:
        id (int): The unique identifier for the comment.
        comment (str): The text content of the comment.
        created_on (datetime): The timestamp when the comment was created.
        task_name (str): The name of the task associated with the comment.
    """
        
    id: int
    comment: str
    created_on: datetime
    task_name: str


class UpdateCommentResponse(BaseModel):
    """
    Represents the response data for updating a comment.
    
    Attributes:
        id (int): The unique identifier for the comment.
    """
    id: int
    new_comment: str
    created_on: datetime
    task_name: str


class CommentResponse(BaseModel):
    """
    Represents the response data for a comment.
    
    Attributes:
        id (int): The unique identifier for the comment.
        comment (str): The text content of the comment.
        created_on (datetime): The timestamp when the comment was created.
        task_name (str): The name of the task associated with the comment.
    """
        
    id: int
    comment: str
    created_on: datetime
    task_name: str
