from repository import TaskRepository
from database import *


task_instance = TaskRepository()


def create_task(task): # TODO: Set type annotation to CreateTaskPayload
    task_instance.add(task.task)
    return{"task":"added"}

def display_tasks():  # method for main
    details = task_instance.get()
    return details

def remove_task(task_id): # method for main
    task_instance.remove(task_id.task_id)
    return{"task":"removed"}