from database import *
from database import Task
from abc import ABC, abstractmethod


class AbstractRepository(
    ABC
):  # Adding Repository Layer between database interface and main interface

    @abstractmethod
    def get(self):
        raise NotImplementedError()

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def remove(self,unique_id : int):
        raise NotImplementedError()


class TaskRepository(AbstractRepository):  # inherits Abstractrepository

    def get(self) -> list[Task]:  # get logic
        details = session.query(Task).all()
        return details

    def add(self, new_task: str):
        new_task_obj = Task(task=new_task)
        session.add(new_task_obj)
        session.commit()
        return new_task_obj

    def remove(self, task_id: int):
        remove_task = (
            session.query(Task).filter(Task.id == task_id).first()
        )
        session.delete(remove_task)
        session.commit()
        return remove_task
