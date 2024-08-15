from fastapi import HTTPException
from models.projects import Project
from models.users import User
from service.user_services import get_user_name
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
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"Project": project.name}


def create_project(payload: CreateProjectPayload, owner_id: int):
    owner = session.query(User).filter(User.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    new_project = project_instance.add(
        payload.project_name,
        payload.project_description,
        owner_id,
        payload.start_date,
        payload.end_date,
    )
    user_name = get_user_name(owner_id)
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


def display_projects(owner_id):  # method for main
    details = project_instance.get(owner_id)
    if not details:
        raise HTTPException(status_code=404, detail="Project not found")
    user_name = get_user_name(owner_id)
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


def remove_project(payload: RemoveProjectPayload, owner_id: int):  # method for main
    delete_project = project_instance.remove(payload.project_id)
    if not delete_project:
        raise HTTPException(status_code=404, detail="Project not found")
    user_name = get_user_name(owner_id)
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


def project_update(payload: UpdateProjectPayload, owner_id: int) -> UpdateProjectResponse:
    updated_project = project_instance.update(
        payload.project_id,
        payload.new_project_name,
        payload.new_project_description,
        payload.start_date,
        payload.end_date,
    )
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    user_name = get_user_name(owner_id)
    return {
        "Updated": UpdateProjectResponse(
            id=updated_project.id,
            name=updated_project.name,
            description=updated_project.description,
            created_at=updated_project.created_at,
            start_date=updated_project.start_date,
            end_date=updated_project.start_date,
            user_name=user_name,
            owner_id=updated_project.owner_id,
        )
    }


def display_project(project_id):
    details = project_instance.getproject(project_id)
    print (details)
    return details
