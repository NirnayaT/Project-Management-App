from fastapi import HTTPException
from config.database import session
from models.images import Image
from schemas.image import ImageCreate
from repository.repository import AbstractRepositoryForImages


class ImageRepository(AbstractRepositoryForImages):
    def create_image(self, image: ImageCreate):
        db_image = Image(
            filename=image.filename,
            path=image.path,
            url=image.url,
            user_id=image.user_id
        )
        session.add(db_image)
        session.commit()
        session.refresh(db_image)
        return db_image
    
    def delete_image(self, image_id: int):
    # Query for the image record by its ID
        db_image = session.query(Image).filter(Image.id == image_id).first()
        
        if db_image:
            # Delete the image record from the database
            session.delete(db_image)
            session.commit()
            return True
        else:
            # Raise an exception or handle the case where the image is not found
            raise HTTPException(status_code=404, detail="Image not found")