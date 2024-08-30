from pydantic import BaseModel
from datetime import datetime

class ImageBase(BaseModel):
    """
    Base model for an image.
    
    Attributes:
        filename (str): The name of the image file.
        url (str): The URL where the image is hosted.
    """
        
    filename: str
    url: str

class ImageCreate(ImageBase):
    """
    Create a new image.
    
    Attributes:
        path (str): The file path where the image is stored.
        user_id (int): The ID of the user who uploaded the image.
    """
        
    path: str
    user_id: int

class ImageOut(ImageBase):
    """
    Represents an image that has been uploaded and stored.
    
    Attributes:
        id (int): The unique identifier for the image.
        upload_date (datetime): The date and time when the image was uploaded.
    """
        
    id: int
    upload_date: datetime
    user_id: int

