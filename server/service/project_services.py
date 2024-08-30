from fastapi import HTTPException
from models.projects import Project
from models.users import User
from schemas.project_payload import (
    CreateProjectPayload,
    RemoveProjectPayload,
    UpdateProjectPayload,
)
from repository.project_repository import ProjectRepository
from config.database import *
from response.project_responses import (
    CreateProjectResponse,
    ProjectResponse,
    RemoveProjectResponse,
    UpdateProjectResponse,
)


project_instance = ProjectRepository()


def get_project_name(project_id: int) -> str:
    """
    Retrieves the name of a project by its ID.
    
    Args:
        project_id (int): The ID of the project to retrieve the name for.
    
    Returns:
        str: The name of the project.
    
    Raises:
        HTTPException: If the project with the given ID is not found.
    """
        
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.name


def create_project(payload: CreateProjectPayload,owner_id: int, user_name: str):
    """
    Creates a new project in the system.
    
    Args:
        payload (CreateProjectPayload): The payload containing the details of the new project.
        owner_id (int): The ID of the user who is creating the project.
        user_name (str): The name of the user who is creating the project.
    
    Returns:
        dict: A dictionary containing the details of the newly created project.
    
    Raises:
        HTTPException: If the owner with the given ID is not found.
    """
        
    owner = session.query(User).filter(User.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    new_project = project_instance.add(
        payload.project_name,
        payload.project_description,
        user_name,
        payload.start_date,
        payload.end_date,
    )
    return {
        "Added": CreateProjectResponse(
            id=new_project.id,
            name=new_project.name,
            description=new_project.description,
            created_at=new_project.created_at,
            start_date=new_project.start_date,
            end_date=new_project.end_date,
            user_name=user_name,
            owner_id=new_project.owner_id,
        )
    }


def display_projects(owner_id, user_name):  # method for main
    """
    Retrieves a list of projects for the given owner ID and returns a response containing the project details.
    
    Args:
        owner_id (int): The ID of the user who owns the projects.
        user_name (str): The name of the user who is requesting the projects.
    
    Returns:
        dict: A dictionary containing a list of `ProjectResponse` objects, each representing a project.
    
    Raises:
        HTTPException: If no projects are found for the given owner ID.
    """
        
    details = project_instance.get(owner_id)
    if not details:
        raise HTTPException(status_code=404, detail="Project not found")
    response = [
        ProjectResponse(
            id=project.id,
            name=project.name,
            description=project.description,
            created_at=project.created_at,
            start_date=project.start_date,
            end_date=project.end_date,
            user_name=user_name,
            owner_id=project.owner_id,
        )
        for project in details
    ]
    return {"Projects": response}


def remove_project(payload: RemoveProjectPayload, user_name: str):  # method for main
    """
    Removes a project from the system based on the provided payload.
    
    Args:
        payload (RemoveProjectPayload): The payload containing the project ID to be removed.
        user_name (str): The name of the user who is requesting the project removal.
    
    Returns:
        dict: A dictionary containing a `RemoveProjectResponse` object, which represents the removed project.
    
    Raises:
        HTTPException: If the project with the provided ID is not found.
    """
        
    delete_project = project_instance.remove(payload.project_id)
    if not delete_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "Removed": RemoveProjectResponse(
            id=delete_project.id,
            name=delete_project.name,
            description=delete_project.description,
            created_at=delete_project.created_at,
            start_date=delete_project.start_date,
            end_date=delete_project.end_date,
            user_name=user_name,
            owner_id=delete_project.owner_id,
        )
    }


def project_update(payload: UpdateProjectPayload, user_name: str) -> UpdateProjectResponse:
    """
    Updates an existing project in the system with the provided payload.
    
    Args:
        payload (UpdateProjectPayload): The payload containing the updated project details.
        user_name (str): The name of the user who is requesting the project update.
    
    Returns:
        UpdateProjectResponse: A response object containing the updated project details.
    
    Raises:
        HTTPException: If the project with the provided ID is not found.
    """
        
    updated_project = project_instance.update(
        project_id=payload.project_id,
        new_project_name=payload.new_project_name,
        new_project_description=payload.new_project_description,
        start_date=payload.start_date,
        end_date=payload.end_date,
    )
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "Updated": UpdateProjectResponse(
            id=updated_project.id,
            name=updated_project.name,
            description=updated_project.description,
            created_at=updated_project.created_at,
            start_date=updated_project.start_date,
            end_date=updated_project.end_date,
            user_name=user_name,
            owner_id=updated_project.owner_id,
        )
    }


def display_project(project_id):
    """
    Retrieves the details of a project with the given project ID.
    
    Args:
        project_id (int): The ID of the project to retrieve.
    
    Returns:
        dict: A dictionary containing the details of the project.
    """
        
    details = project_instance.get_project(project_id)
    return details
