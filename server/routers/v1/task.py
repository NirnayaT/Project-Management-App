from fastapi import APIRouter
from models.users import User
from utils.tokens.jwt_handler import get_current_user
from response.task_responses import TaskResponse
from service.task_services import (
    display_tasks,
    create_task,
    display_tasks_user,
    remove_task,
    task_update,
)
from schemas.task_payload import (
    CreateTaskPayload,
    RemoveTaskPayload,
    UpdateTaskPayload,
)
from fastapi import Depends


router = APIRouter(prefix="/tasks", tags=["Task Management"])


@router.post("/add")
def add_task(task: CreateTaskPayload, current_user: User = Depends(get_current_user)):
    """
    Adds a new task to the system.
    
    Args:
        task (CreateTaskPayload): The details of the task to be created.
        current_user (User): The user creating the task, obtained 
        from the current user token.
    
    Returns:
        The created task.
    """
        
    return create_task(task)


@router.get(
    "/show",
    response_model=list[TaskResponse],
)
def show_tasks(project_id, current_user: User = Depends(get_current_user)):
    """
    Retrieves and returns a list of tasks for the specified project.
    
    Args:
        project_id (int): The ID of the project to retrieve tasks for.
        current_user (User): The current user, obtained from the user token.
    
    Returns:
        list[TaskResponse]: A list of task responses for the specified 
        project.
    """
        
    return display_tasks(project_id)


@router.get(
    "/show/user",
    response_model=list[TaskResponse],
)
def show_user_task(current_user: User = Depends(get_current_user)):
    """
    Retrieves and returns a list of tasks for the specified user.
    
    Args:
        current_user (User): The current user, obtained from the user 
        token.
    
    Returns:
        list[TaskResponse]: A list of task responses for the specified 
        user.
    """
        
    return display_tasks_user(current_user.id)


@router.delete("/remove")
def delete_task(
    payload: RemoveTaskPayload, current_user: User = Depends(get_current_user)
):
    """
    Deletes a task based on the provided payload.
    
    Args:
        payload (RemoveTaskPayload): The details of the task to be deleted.
        current_user (User): The user deleting the task, obtained from the 
        current user token.
    
    Returns:
        The result of the task deletion operation.
    """
        
    return remove_task(payload)


@router.patch("/update")
def update_task(
    payload: UpdateTaskPayload, current_user: User = Depends(get_current_user)
):
    """
    Updates a task based on the provided payload.
    
    Args:
        payload (UpdateTaskPayload): The details of the task to be updated.
        current_user (User): The user updating the task, obtained from the 
        current user token.
    
    Returns:
        The result of the task update operation.
    """
        
    return task_update(payload)
