from fastapi import FastAPI
from services import create_task, display_tasks, remove_task

app=FastAPI()

@app.get("/")
def root():
    return{"Welcome to":"To-Do-App"}

@app.get("/tasks")
def show_tasks():
    return display_tasks()

@app.post("/tasks/{task}")
def add_task(task:str):
    return create_task(task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    return remove_task(task_id)