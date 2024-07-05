from fastapi import APIRouter
from tasks.services import display_tasks, create_task, remove_task, task_update
from tasks.payload import (
    CreateTaskPayload,
    RemoveTaskPayload,
    ShowTaskPayload,
    UpdateTaskPayload,
)
from fastapi import Depends
from Users.auth.jwt_bearer import jwtBearer

router = APIRouter()


@router.get("/tasks", dependencies=[Depends(jwtBearer())])
def show_tasks(payload: ShowTaskPayload):
    return display_tasks(payload)


@router.post("/tasks", dependencies=[Depends(jwtBearer())])
def add_task(task: CreateTaskPayload):
    return create_task(task)


@router.delete("/tasks", dependencies=[Depends(jwtBearer())])
def delete_task(payload: RemoveTaskPayload):
    show_payload = ShowTaskPayload(project_id=payload.project_id)
    return remove_task(payload), display_tasks(show_payload)


@router.put("/tasks", dependencies=[Depends(jwtBearer())])
def update_task(payload: UpdateTaskPayload):
    show_payload = ShowTaskPayload(project_id=payload.project_id)
    return task_update(payload), display_tasks(show_payload)
