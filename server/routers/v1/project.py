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
    return create_project(payload, current_user.id, current_user.username)


@router.get("/show")
def show_projects(current_user: User = Depends(get_current_user)):
    return display_projects(current_user.id, current_user.username)


@router.patch("/update")
def update_project(
    payload: UpdateProjectPayload, current_user: User = Depends(get_current_user)
):
    return project_update(payload, current_user.username)


@router.delete("/remove")
def delete_project(
    payload: RemoveProjectPayload, current_user: User = Depends(get_current_user)
):
    return remove_project(payload, current_user.username)


@router.get("/project/show")
def get_project(project_id: int, current_user: User = Depends(get_current_user)):
    return display_project(project_id)
