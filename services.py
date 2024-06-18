from repository import TaskRepository
from database import *

task_instance = TaskRepository()


def create_task(task):  # method for main
    added_details= task_instance.add(task)
    return added_details

def display_tasks():  # method for main
    details = task_instance.get()
    return details


def remove_task(task):  # method for main
    removed_task = task_instance.remove(task)
    return removed_task