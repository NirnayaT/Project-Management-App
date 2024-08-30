from datetime import datetime
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.database import Base


class Project(Base):
    """
    Represents a project in the application. A project has a name, description, creation date, owner, start date, and end date. It is associated with one or more tasks.
    """

    __tablename__ = "projects"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    owner_id = Column(Integer(), ForeignKey("users.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")
