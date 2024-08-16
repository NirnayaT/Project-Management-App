from datetime import date
from config.database import session
from config.enumeration import TaskPriority, TaskStatus
from repository.repository import AbstractRepository
from fastapi import HTTPException
from models.tasks import Task


class TaskRepository(AbstractRepository):  # inherits Abstractrepository

    def get(self, project_id: int) -> list[Task]:  # get logic
        details = session.query(Task).filter(Task.project_id == project_id).all()
        return details
        

    def add(
        self,
        project_id: int,
        new_task: str,
        status: str,
        priority: str,
        assignee_id: int,
        due_date: date,
    ):
        print(status.upper())
        status = TaskStatus(status.upper())
        priority = TaskPriority(priority.upper())

        new_task_obj = Task(
            task=new_task,
            project_id=project_id,
            status=status,
            priority=priority,
            assignee_id=assignee_id,
            due_date=due_date,
        )
        # print(project_id,status,priority,assignee_id,due_date)
        try:
            session.add(new_task_obj)
            # print(new_task_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=f"Unable to add taks.{e}")
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

    def update(
        self,
        project_id: int,
        task_id: int,
        new_task: str,
        status: str,
        priority: str,
        assignee_id: int,
        due_date: date,
    ):
        status = TaskStatus(status.upper())
        priority = TaskPriority(priority.upper())
        update_task = (
            session.query(Task)
            .filter(Task.id == task_id, Task.project_id == project_id)
            .first()
        )
        if update_task:
            update_task.task = new_task
            update_task.status = status
            update_task.priority = priority
            update_task.assignee_id = assignee_id
            update_task.due_date = due_date
            session.commit()
        return update_task
