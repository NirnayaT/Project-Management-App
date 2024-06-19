from fastapi import FastAPI
from services import create_task, display_tasks, remove_task
from pydantic import BaseModel

class CreateTaskPayload(BaseModel):
    task : str

class RemoveTaskPayload(BaseModel):
    task_id : int

app=FastAPI()

@app.get("/tasks")
def show_tasks():
    return display_tasks()

@app.post("/tasks")
def add_task(task: CreateTaskPayload):
    return create_task(task), display_tasks()

@app.delete("/tasks")
def delete_task(task_id: RemoveTaskPayload):
    return remove_task(task_id), display_tasks()