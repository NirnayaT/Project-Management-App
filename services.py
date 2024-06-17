from functions import TaskRepository
from database import *


def create_task():#method for main
    add_ins = TaskRepository()
    task = input("Enter the task: ")
    add_ins.add(task)

def display_tasks():#method for main
    get_ins = TaskRepository()
    details = get_ins.get()
    for d in details:
        print(d.id,'.',d.task)

def remove_task():#method for main
    remove_ins = TaskRepository()
    task = int(input("Enter the no to remove: "))
    remove_ins.remove(task)

