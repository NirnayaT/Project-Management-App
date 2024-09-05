from fastapi import APIRouter
from service.comment_services import (
    display_comments,
    create_comment,
    remove_comment,
    update_comment as update_comment_route,
)
from schemas.comment_payload import (
    CreateCommentPayload,
    RemoveCommentPayload,
    UpdateCommentPayload,
)
from fastapi import Depends

from models.users import User
from utils.tokens.jwt_handler import get_current_user

# from Users.auth.dependencies import get_current_user


router = APIRouter(
    tags=["Comment Management"]
)


@router.post("/comments/add")
async def add_comment(comment: CreateCommentPayload, current_user: User = Depends(get_current_user)):
    """
    Add a new comment to a task.
    
    Args:
        comment (CreateCommentPayload): The comment payload 
        containing the task ID and comment text.
        current_user (User): The current authenticated user.
    
    Returns:
        The created comment.
    """
    return await create_comment(comment, current_user.id)


@router.get("/comments/show")
async def show_comments(task_id, current_user: User = Depends(get_current_user)):
    """
    Display the comments for a given task.
    
    Args:
        task_id (int): The ID of the task to retrieve comments for.
        current_user (User): The current authenticated user.
    
    Returns:
        The list of comments for the specified task.
    """
        
    return await display_comments(task_id)


@router.delete("/comments/remove")
async def delete_comment(payload: RemoveCommentPayload, current_user: User = Depends(get_current_user)):
    """
    Delete a comment for a given task.
    
    Args:
        payload (RemoveCommentPayload): The payload containing the 
        ID of the comment to be deleted and the ID of the task.
        current_user (User): The current authenticated user.
    
    Returns:
        The result of removing the comment and the updated list of 
        comments for the specified task.
    """
        
    return await remove_comment(payload), await display_comments(payload.task_id)


@router.put("/comments/update")
async def update_comment(payload: UpdateCommentPayload, current_user: User = Depends(get_current_user)):
    """
    Update a comment for a given task.
    
    Args:
        payload (UpdateCommentPayload): The payload containing the 
        ID of the comment to be updated, the updated comment text, 
        and the ID of the task.
        
        current_user (User): The current authenticated user.
    
    Returns:
        The result of updating the comment and the updated list of 
        comments for the specified task.
    """
        
    return await update_comment_route(payload), await display_comments(payload.task_id)
