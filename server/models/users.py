from sqlalchemy import Boolean, Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    """
    Represents a user in the application. Each user has a unique email address
    , a username, a hashed password, and flags indicating whether the user is 
    active and verified.
    
    Users can be associated with projects, tasks, and images through 
    relationships.
    """
        
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_verified = Column(Boolean(), default=False)
    __table_args__ = (UniqueConstraint("email", name="unique_user_constraint"),)
    projects = relationship("Project", back_populates="owner")
    tasks_assigned = relationship("Task", back_populates="assignee")
    images = relationship("Image", back_populates="user")
