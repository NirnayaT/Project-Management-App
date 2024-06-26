from fastapi import HTTPException
from Project.repository import ProjectRepository
from Database.database import *
from Project.responses import CreateProjectResponse, RemoveProjectResponse, UpdateProjectResponse


project_instance = ProjectRepository()

def get_project_name(project_id: int) -> str:
    project = session.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project.name

def create_project(name: str, description: str, owner_id: int):  
    owner = session.query(User).filter(User.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    new_project = project_instance.add(name, description, owner_id)
    return CreateProjectResponse(
        id=new_project.id,
        name=new_project.name,
        description=new_project.description,
        created_at=new_project.created_at,
    )


def display_projects():  # method for main
    details = project_instance.get()
    return details


def remove_project(project_id):  # method for main
    delete_project = project_instance.remove(project_id.project_id)
    if not delete_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return RemoveProjectResponse(
        id=delete_project.id,
        name=delete_project.name,
        description=delete_project.description,
        created_at=delete_project.created_at,
    )


def project_update(project_id: int, new_project_name: str, new_project_decription: str) -> UpdateProjectResponse:
    updated_project = project_instance.update(project_id, new_project_name, new_project_decription)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return UpdateProjectResponse(
        id=updated_project.id,
        name=updated_project.name,
        description=updated_project.description,
        created_at=updated_project.created_at,
    )
