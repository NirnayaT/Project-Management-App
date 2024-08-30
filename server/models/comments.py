from datetime import datetime
from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Comment(Base):
    """
    Represents a comment associated with a task in the application.
    
    Attributes:
        id (int): The unique identifier for the comment.
        comment (str): The text content of the comment.
        created_at (datetime): The timestamp when the comment was created.
        task_id (int): The identifier of the task the comment is associated with.
        owner_id (int): The identifier of the user who created the comment.
        task (Task): The task the comment is associated with.
        user (User): The user who created the comment.
    """
        
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    task = relationship("Task", back_populates="comments")
    user = relationship("User")
