from datetime import datetime
from sqlalchemy import Column, String, Integer, Enum, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.enumeration import TaskPriority, TaskStatus
from config.database import Base


class Task(Base):
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
