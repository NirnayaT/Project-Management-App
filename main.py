from fastapi import FastAPI

from tasks.payload import CreateTaskPayload, RemoveTaskPayload
import tasks.services as task_services


app = FastAPI()


@app.get("/tasks")
def show_tasks():
    return task_services.display_tasks()


@app.post("/tasks")
def add_task(task: CreateTaskPayload):
    return task_services.create_task(task), task_services.display_tasks()


@app.delete("/tasks")
def delete_task(task_id: RemoveTaskPayload):
    return task_services.remove_task(task_id), task_services.display_tasks()
