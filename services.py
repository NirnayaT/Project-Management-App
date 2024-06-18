from repository import TaskRepository
from database import *

task_instance = TaskRepository()


def create_task():  # method for main
    task = input("Enter the task: ")
    task_instance.add(task)


def display_tasks():  # method for main
    details = task_instance.get()
    for d in details:
        print(d.id, ".", d.task)


def remove_task():  # method for main
    task = int(input("Enter the no to remove: "))
    task_instance.remove(task)
