from fastapi import APIRouter
from models.users import User
from utils.auth.jwt_handler import get_current_user
from response.task_responses import TaskResponse
from service.task_services import display_tasks, create_task, remove_task, task_update
from schemas.task_payload import (
    CreateTaskPayload,
    RemoveTaskPayload,
    UpdateTaskPayload,
)
from fastapi import Depends


router = APIRouter(
    prefix="/tasks",
    tags=["Task Management"]
)


@router.post("/add")
def add_task(task: CreateTaskPayload, current_user: User = Depends(get_current_user)):
    return create_task(task)


@router.get(
    "/show",
    response_model=list[TaskResponse],
)
def show_tasks(project_id, current_user: User = Depends(get_current_user)):
    return display_tasks(project_id)


@router.delete("/remove")
def delete_task(payload: RemoveTaskPayload, current_user: User = Depends(get_current_user)):
    return remove_task(payload)


@router.put("/update")
def update_task(payload: UpdateTaskPayload, current_user: User = Depends(get_current_user)):
    return task_update(payload)
