from datetime import datetime
from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    task = relationship("Task", back_populates="comments")
    user = relationship("User")
