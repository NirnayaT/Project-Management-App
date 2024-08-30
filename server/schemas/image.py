from pydantic import BaseModel
from datetime import datetime

class ImageBase(BaseModel):
    filename: str
    url: str

class ImageCreate(ImageBase):
    path: str
    user_id: int

class ImageOut(ImageBase):
    id: int
    upload_date: datetime
    user_id: int

