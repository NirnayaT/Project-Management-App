from tasks.repository import TaskRepository
from Database.database import *
from tasks.responses import CreateTaskResponse, RemoveTaskResponse


task_instance = TaskRepository()


def create_task(task):  # TODO: Set type annotation to CreateTaskPayload
    new_task = task_instance.add(task.task)

    return CreateTaskResponse(
        id=new_task.id,
        task=new_task.task,
        is_complete=new_task.is_complete,
        created_on=new_task.created_on,
    )


def display_tasks():  # method for main
    details = task_instance.get()
    return details


def remove_task(task_id):  # method for main
    delete_task = task_instance.remove(task_id.task_id)
    return RemoveTaskResponse(
        id=delete_task.id,
        task=delete_task.task,
        is_complete=delete_task.is_complete,
        created_on=delete_task.created_on,
    )
