from datetime import date
from config.database import session
from config.enumeration import TaskPriority, TaskStatus
from repository.repository import AbstractRepository
from fastapi import HTTPException
from models.tasks import Task
from models.users import User
from sqlalchemy import and_

class TaskRepository(AbstractRepository):  # inherits Abstractrepository
    """
    Provides a repository for managing tasks, including functionality to:
    - Get tasks by project ID or user ID
    - Add a new task
    - Remove a task
    - Update an existing task
    """
        
    def get(self, project_id: int) -> list[Task]:
        """
        Retrieves a list of tasks associated with the specified project ID.
        
        Args:
            project_id (int): The ID of the project to retrieve tasks for.
        
        Returns:
            list[Task]: A list of Task objects associated with the 
            specified project ID.
        """
                
        details = session.query(Task).filter(Task.project_id == project_id).all()
        return details


    def get_by_user(self, user_id: int) -> list[Task]: 
        """
        Retrieves a list of tasks associated with the specified user ID.
        
        Args:
            user_id (int): The ID of the user to retrieve tasks for.
        
        Returns:
            list[Task]: A list of Task objects associated with the 
            specified user ID.
        """
                
        details = session.query(Task).filter(Task.assignee_id == user_id).all()
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
        """
        Adds a new task to the database.
        
        Args:
            project_id (int): The ID of the project the task belongs to.
            new_task (str): The text of the new task.
            status (str): The status of the new task.
            priority (str): The priority of the new task.
            assignee_id (int): The ID of the user the task is assigned to.
            due_date (date): The due date of the new task.
        
        Returns:
            Task: The newly created task object.
        
        Raises:
            HTTPException: If there is an error adding the task to the 
            database.
        """
                
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
        """
        Removes a task from the database.
        
        Args:
            project_id (int): The ID of the project the task belongs to.
            task_id (int): The ID of the task to remove.
        
        Returns:
            Task: The removed task object, or None if the task was not found.
        """
                
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
        """
        Updates an existing task in the database.
        
        Args:
            project_id (int): The ID of the project the task 
            belongs to.
            task_id (int): The ID of the task to update.
            new_task (str): The new task text.
            status (str): The new task status.
            priority (str): The new task priority.
            assignee_id (int): The new assignee ID.
            due_date (date): The new due date.
        
        Returns:
            Task: The updated task object, or None if the task was not 
            found.
        
        Raises:
            HTTPException: If there is an error updating the task in the 
            database.
        """
                
        if status is not None:
            status = TaskStatus(status.upper())
        if priority is not None:
            priority = TaskPriority(priority.upper())
        update_task = (
            session.query(Task)
            .filter(Task.id == task_id, Task.project_id == project_id)
            .first()
        )
        if update_task:
            if new_task is not None:
                update_task.task = new_task
            if status is not None:
                update_task.status = status
            if priority is not None:
                update_task.priority = priority
            if assignee_id is not None:
                update_task.assignee_id = assignee_id
            if due_date is not None:
                update_task.due_date = due_date
            print(update_task.due_date)
            session.commit()
        return update_task
