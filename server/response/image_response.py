from pydantic import BaseModel
from datetime import datetime

class ImageResponse(BaseModel):
    id: int
    filename: str
    url: str
    upload_date: datetime
