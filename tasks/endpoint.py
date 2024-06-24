from fastapi import APIRouter
from tasks.services import display_tasks, create_task, remove_task
from tasks.payload import CreateTaskPayload, RemoveTaskPayload
from fastapi import Depends
from Users.auth.jwt_bearer import jwtBearer

router = APIRouter()

@router.get("/tasks")
def show_tasks():
    return display_tasks()

@router.post("/tasks",dependencies=[Depends(jwtBearer())])
def add_task(task: CreateTaskPayload):
    return create_task(task), display_tasks()

@router.delete("/tasks",dependencies=[Depends(jwtBearer())])
def delete_task(task_id: RemoveTaskPayload):
    return remove_task(task_id), display_tasks()