from Database.database import Task, session
from Database.enumeration import TaskStatus
from repository import AbstractRepository
from fastapi import HTTPException


class TaskRepository(AbstractRepository):  # inherits Abstractrepository

    def get(self, project_id: int) -> list[Task]:  # get logic
        details = session.query(Task).filter(Task.project_id == project_id).all()
        return details

    def add(self, project_id: int, new_task: str, is_complete: str):
        status = TaskStatus(is_complete.upper())
        new_task_obj = Task(task=new_task, project_id=project_id, is_complete=status)
        try:
            session.add(new_task_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=f"Unable to add tasks: {e}")
        return new_task_obj

    def remove(self, project_id: int, task_id: int):
        remove_task = (
            session.query(Task)
            .filter(Task.id == task_id, Task.project_id == project_id)
            .first()
        )
        if remove_task:
            session.delete(remove_task)
            session.commit()
        return remove_task

    def update(self, project_id: int, task_id: int, new_task: str, is_complete: str):
        status = TaskStatus(is_complete.upper())
        update_task = (
            session.query(Task)
            .filter(Task.id == task_id, Task.project_id == project_id)
            .first()
        )
        if update_task:
            update_task.task = new_task
            update_task.is_complete = status
            session.commit()
        return update_task
