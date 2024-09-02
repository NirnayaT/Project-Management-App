from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base

class Image(Base):
    """
        Represents an image stored in the database.
        
        Attributes:
            id (int): The unique identifier for the image.
            filename (str): The filename of the image, which must be unique.
            path (str): The file path where the image is stored.
            url (str): The URL where the image can be accessed.
            upload_date (datetime): The date and time when the image was uploaded.
            user_id (int): The ID of the user who uploaded the image.
            user (User): The user who uploaded the image, accessed through a relationship.
        """
                
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True, nullable=False)
    path = Column(String, nullable=False)
    url = Column(String, nullable=False)  
    upload_date = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="images")
