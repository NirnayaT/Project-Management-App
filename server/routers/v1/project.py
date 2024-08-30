from fastapi import APIRouter
from models.users import User
from response.project_responses import UpdateProjectResponse
from service.project_services import (
    display_projects,
    create_project,
    remove_project,
    project_update,
    display_project,
)
from schemas.project_payload import (
    CreateProjectPayload,
    RemoveProjectPayload,
    UpdateProjectPayload,
)
from fastapi import Depends

from utils.tokens.jwt_handler import get_current_user

# from Users.auth.dependencies import get_current_user


router = APIRouter(prefix="/projects", tags=["Project Management"])


@router.post("/create")
def add_project(
    payload: CreateProjectPayload, current_user: User = Depends(get_current_user)
):
    """
    Adds a new project for the current user.
    
    Args:
        payload (CreateProjectPayload): The payload containing the details of the new project.
        current_user (User): The current authenticated user.
    
    Returns:
        The response from the `create_project` function, which likely includes the newly created project.
    """
        
    return create_project(payload, current_user.id, current_user.username)


@router.get("/show")
def show_projects(current_user: User = Depends(get_current_user)):
    """
    Retrieves a list of projects for the current authenticated user.
    
    Args:
        current_user (User): The current authenticated user.
    
    Returns:
        The response from the `display_projects` function, which likely includes a list of projects for the current user.
    """
        
    return display_projects(current_user.id, current_user.username)


@router.patch("/update")
def update_project(
    payload: UpdateProjectPayload, current_user: User = Depends(get_current_user)
):
    """
    Updates an existing project for the current authenticated user.
    
    Args:
        payload (UpdateProjectPayload): The payload containing the updated details of the project.
        current_user (User): The current authenticated user.
    
    Returns:
        The response from the `project_update` function, which likely includes the updated project details.
    """
        
    return project_update(payload, current_user.username)


@router.delete("/remove")
def delete_project(
    payload: RemoveProjectPayload, current_user: User = Depends(get_current_user)
):
    """
    Deletes an existing project for the current authenticated user.
    
    Args:
        payload (RemoveProjectPayload): The payload containing the details of the project to be deleted.
        current_user (User): The current authenticated user.
    
    Returns:
        The response from the `remove_project` function, which likely includes the result of the delete operation.
    """
        
    return remove_project(payload, current_user.username)


@router.get("/project/show")
def get_project(project_id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieves the details of a specific project for the current authenticated user.
    
    Args:
        project_id (int): The ID of the project to retrieve.
        current_user (User): The current authenticated user.
    
    Returns:
        The response from the `display_project` function, which likely includes the details of the requested project.
    """
        
    return display_project(project_id)
