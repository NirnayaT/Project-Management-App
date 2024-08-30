from datetime import datetime
from sqlalchemy import Column, String, Integer, Enum, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.enumeration import TaskPriority, TaskStatus
from config.database import Base


class Task(Base):
    """
    Defines the Task model, which represents a task in a project. The Task model has the following fields:
    
    - id (Integer): The unique identifier for the task.
    - task (String): The title or description of the task.
    - status (TaskStatus): The current status of the task, which can be one of the values defined in the TaskStatus enumeration.
    - created_on (DateTime): The date and time when the task was created.
    - project_id (Integer): The ID of the project that the task belongs to.
    - due_date (Date): The date when the task is due.
    - priority (TaskPriority): The priority of the task, which can be one of the values defined in the TaskPriority enumeration.
    - assignee_id (Integer): The ID of the user who is assigned to the task.
    
    The Task model has the following relationships:
    
    - project (Project): The project that the task belongs to.
    - comments (Comment): The comments associated with the task.
    - assignee (User): The user who is assigned to the task.
    """
        
    __tablename__ = "tasks"
    id = Column(Integer(), primary_key=True)
    task = Column(String(100), nullable=False)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.TODO)
    created_on = Column(DateTime(), default=datetime.now)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    due_date = Column(Date, nullable=True)
    priority = Column(Enum(TaskPriority), nullable=False, default=TaskPriority.MEDIUM)
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    project = relationship("Project", back_populates="tasks")
    comments = relationship("Comment", back_populates="task")
    assignee = relationship("User", back_populates="tasks_assigned")
