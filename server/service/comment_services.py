from fastapi import HTTPException
from service.task_services import get_task_name
from schemas.comment_payload import (
    CreateCommentPayload,
    RemoveCommentPayload,
    UpdateCommentPayload,
)
from repository.comment_repository import CommentRepository
from config.database import *
from response.comment_responses import (
    CreateCommentResponse,
    RemoveCommentResponse,
    CommentResponse,
    UpdateCommentResponse,
)
from utils.sockets.manager import manager

comment_instance = CommentRepository()


async def create_comment(comment_payload: CreateCommentPayload, owner_id : int):
    """
    Adds a new comment to a task and broadcasts the new comment to connected clients.
    
    Args:
        comment_payload (CreateCommentPayload): The payload containing the comment text and task ID.
        owner_id (int): The ID of the user who is creating the comment.
    
    Returns:
        CreateCommentResponse: A response object containing the details of the newly created comment.
    """
        
    new_comment = comment_instance.add(
        comment=comment_payload.comment,
        task_id=comment_payload.task_id,
        owner_id=owner_id
    )
    task_name = get_task_name(comment_payload.task_id)
    response = CreateCommentResponse(
        id=new_comment.id,
        comment=new_comment.comment,
        created_on=new_comment.created_at,
        task_name=task_name,
    )
    await manager.broadcast(f"New comment added: {response.comment}")
    return response


async def remove_comment(payload: RemoveCommentPayload) -> RemoveCommentResponse:
    """
    Removes a comment from a task and broadcasts the removal to connected clients.
    
    Args:
        payload (RemoveCommentPayload): The payload containing the task ID and comment ID of the comment to be removed.
    
    Returns:
        RemoveCommentResponse: A response object containing the details of the removed comment.
    
    Raises:
        HTTPException: If the comment is not found(404).
    """

    delete_comment = comment_instance.remove(payload.task_id, payload.comment_id)
    if not delete_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    task_name = get_task_name(payload.task_id)
    response = RemoveCommentResponse(
        id=delete_comment.id,
        comment=delete_comment.comment,
        created_on=delete_comment.created_at,
        task_name=task_name,
    )
    await manager.broadcast(f"Comment removed: {response.comment}")
    return response


async def update_comment(payload: UpdateCommentPayload) -> UpdateCommentResponse:
    """
    Updates an existing comment for a task and broadcasts the update to connected clients.
    
    Args:
        payload (UpdateCommentPayload): The payload containing the task ID, comment ID, and the new comment text.
    
    Returns:
        UpdateCommentResponse: A response object containing the details of the updated comment.
    
    Raises:
        HTTPException: If the comment is not found(404).
    """
        
    updated_comment = comment_instance.update(
        payload.task_id, payload.comment_id, payload.new_comment
    )
    if not updated_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    task_name = get_task_name(payload.task_id)
    response = UpdateCommentResponse(
        id=updated_comment.id,
        new_comment=updated_comment.comment,
        created_on=updated_comment.created_at,
        task_name=task_name,
    )
    await manager.broadcast(f"Comment updated: {response.new_comment}")
    return response


async def display_comments(task_id):  # method for main
    """
    Retrieves and returns the comments for the specified task.
    
    Args:
        task_id (str): The ID of the task to retrieve comments for.
    
    Returns:
        dict: A dictionary containing a list of CommentResponse objects, each representing a comment for the specified task.
    """
        
    details = comment_instance.get(task_id)
    task_name = get_task_name(task_id)
    response = [
        CommentResponse(
            id=comments.id,
            comment=comments.comment,
            created_on=comments.created_at,
            task_name=task_name,
        )
        for comments in details
    ]
    return {"Comments": response}
