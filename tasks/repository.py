from Database.database import Task, session
from repository import AbstractRepository


class TaskRepository(AbstractRepository):  # inherits Abstractrepository

    def get(self, project_id: int) -> list[Task]:  # get logic
        details = session.query(Task).filter(Task.project_id == project_id).all()
        return details

    def add(self, project_id: int, new_task: str):
        new_task_obj = Task(task=new_task, project_id=project_id)
        session.add(new_task_obj)
        session.commit()
        return new_task_obj

    def remove(self, project_id: int, task_id: int):
        remove_task = (
            session.query(Task)
            .filter(Task.id == task_id, Task.project_id == project_id)
            .first()
        )
        session.delete(remove_task)
        session.commit()
        return remove_task

    def update(self, project_id: int, task_id: int, new_task: str):
        update_task = (
            session.query(Task)
            .filter(Task.id == task_id, Task.project_id == project_id)
            .first()
        )
        if update_task:
            update_task.task = new_task
            session.commit()
        return update_task