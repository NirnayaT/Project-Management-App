from pydantic import BaseModel
from datetime import datetime

class ImageResponse(BaseModel):
    """
    Represents the response data for an uploaded image.
    
    :param id: The unique identifier for the image.
    :param filename: The name of the image file.
    :param url: The URL where the image can be accessed.
    :param upload_date: The date and time when the image was uploaded.
    """
        
    id: int
    filename: str
    url: str
    upload_date: datetime
