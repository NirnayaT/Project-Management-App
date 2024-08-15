from sqlalchemy import Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    __table_args__ = (UniqueConstraint("email", name="unique_user_constraint"),)
    projects = relationship("Project", back_populates="owner")
    tasks_assigned = relationship("Task", back_populates="assignee")
