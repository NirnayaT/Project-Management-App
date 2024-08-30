from fastapi import HTTPException
from models.tasks import Task
from service.project_services import get_project_name
from schemas.task_payload import (
    CreateTaskPayload,
    RemoveTaskPayload,
    UpdateTaskPayload,
)
from repository.task_repository import TaskRepository
from config.database import *
from response.task_responses import (
    CreateTaskResponse,
    RemoveTaskResponse,
    UpdateTaskResponse,
)


task_instance = TaskRepository()


def get_task_name(task_id: int) -> str:
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.task


def create_task(
    task_payload: CreateTaskPayload,
) -> list[CreateTaskResponse]:
    new_task = task_instance.add(
        task_payload.project_id,
        task_payload.task,
        task_payload.status,
        task_payload.priority,
        task_payload.assignee_id,
        task_payload.due_date,
    )
    # project_name = get_project_name(task_payload.project_id)
    return {
        "Added": CreateTaskResponse(
            id=new_task.id,
            task=new_task.task,
            status=new_task.status,
            created_on=new_task.created_on,
            priority=new_task.priority,
            assignee_id=new_task.assignee_id,
            due_date=new_task.due_date,
            # project_name=project_name,
            project_id=new_task.project_id,
        )
    }


def display_tasks(project_id):  # method for main
    details = task_instance.get(project_id)
    return details

def display_tasks_user(user_id):  # method for main
    details = task_instance.get_by_user(user_id)
    return details


def remove_task(payload: RemoveTaskPayload):  # method for main
    delete_task = task_instance.remove(payload.project_id, payload.task_id)
    if not delete_task:
        raise HTTPException(status_code=404, detail="Task not found")
    project_name = get_project_name(payload.project_id)
    return {
        "Removed": RemoveTaskResponse(
            id=delete_task.id,
            task=delete_task.task,
            status=delete_task.status,
            created_on=delete_task.created_on,
            priority=delete_task.priority,
            assignee_id=delete_task.assignee_id,
            due_date=delete_task.due_date,
            project_name=project_name,
            project_id=delete_task.project_id,
        )
    }


def task_update(payload: UpdateTaskPayload) -> UpdateTaskResponse:
    updated_task = task_instance.update(
        project_id=payload.project_id,
        task_id=payload.task_id,
        new_task=payload.new_task,
        status=payload.status,
        priority=payload.priority,
        assignee_id=payload.assignee_id,
        due_date=payload.due_date,
    )
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    project_name = get_project_name(payload.project_id)
    return {
        "Updated": UpdateTaskResponse(
            id=updated_task.id,
            new_task=updated_task.task,
            status=updated_task.status,
            created_on=updated_task.created_on,
            project_name=project_name,
            priority=updated_task.priority,
            assignee_id=updated_task.assignee_id,
            due_date=updated_task.due_date,
            project_id=updated_task.project_id,
        )
    }
