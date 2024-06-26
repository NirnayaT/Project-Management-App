from fastapi import HTTPException
from Project.services import get_project_name
from tasks.payload import CreateTaskPayload, RemoveTaskPayload, UpdateTaskPayload
from tasks.repository import TaskRepository
from Database.database import *
from tasks.responses import CreateTaskResponse, RemoveTaskResponse, TaskResponse, UpdateTaskResponse


task_instance = TaskRepository()


def create_task(
    task_payload: CreateTaskPayload
):  # TODO: Set type annotation to CreateTaskPayload
    new_task = task_instance.add(task_payload.project_id, task_payload.task)
    project_name = get_project_name(task_payload.project_id)
    return CreateTaskResponse(
        id=new_task.id,
        task=new_task.task,
        is_complete=new_task.is_complete,
        created_on=new_task.created_on,
        project_name=project_name
    )


def display_tasks(project_id: int):  # method for main
    details = task_instance.get(project_id)
    project_name = get_project_name(project_id)
    response = [TaskResponse(
        id=task.id,
        task=task.task,
        is_complete=task.is_complete,
        created_on=task.created_on,
        project_name=project_name
    ) for task in details  
    ]
    return details


def remove_task(payload: RemoveTaskPayload) -> RemoveTaskResponse:  # method for main
    delete_task = task_instance.remove(payload.project_id, payload.task_id)
    if not delete_task:
        raise HTTPException(status_code=404, detail="Task not found")
    project_name = get_project_name(payload.project_id)
    return RemoveTaskResponse(
        id=delete_task.id,
        task=delete_task.task,
        is_complete=delete_task.is_complete,
        created_on=delete_task.created_on,
        project_name=project_name
    )


def task_update(payload: UpdateTaskPayload) -> UpdateTaskResponse:
    updated_task = task_instance.update(payload.project_id, payload.task_id, payload.new_task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    project_name = get_project_name(payload.project_id)
    return UpdateTaskResponse(
        id=updated_task.id,
        new_task=updated_task.task,
        is_complete=updated_task.is_complete,
        created_on=updated_task.created_on,
        project_name=project_name
    )
