from fastapi import APIRouter
from tasks.services import display_tasks, create_task, remove_task, task_update
from tasks.payload import CreateTaskPayload, RemoveTaskPayload, UpdateTaskPayload
from fastapi import Depends
from Users.auth.jwt_bearer import jwtBearer

router = APIRouter()


@router.get("/tasks")
def show_tasks(project_id: int):
    return display_tasks(project_id)


@router.post("/tasks", dependencies=[Depends(jwtBearer())])
def add_task(task: CreateTaskPayload):
    return create_task(task)


@router.delete("/tasks", dependencies=[Depends(jwtBearer())])
def delete_task(payload: RemoveTaskPayload):
    return remove_task(payload), display_tasks(payload.project_id)


@router.put("/tasks", dependencies=[Depends(jwtBearer())])
def update_task(payload: UpdateTaskPayload):
    return task_update(payload), display_tasks(payload.project_id)