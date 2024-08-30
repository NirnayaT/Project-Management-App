from fastapi import HTTPException
from config.database import session
from models.images import Image
from schemas.image import ImageCreate
from repository.repository import AbstractRepositoryForImages


class ImageRepository(AbstractRepositoryForImages):
    """
    Provides an implementation of the `AbstractRepositoryForImages` interface for managing image data in the database.
    
    The `ImageRepository` class provides methods for creating and deleting image records in the database.
    
    The `create_image` method takes an `ImageCreate` schema object and creates a new `Image` record in the database, committing the changes and returning the created `Image` object.
    
    The `delete_image` method takes an `image_id` integer and deletes the corresponding `Image` record from the database, if it exists. If the image is not found, it raises an `HTTPException` with a 404 status code.
    """
        
    def create_image(self, image: ImageCreate):
        """
        Creates a new image record in the database based on the provided `ImageCreate` schema.
        
        Args:
            image (ImageCreate): The image data to be created.
        
        Returns:
            Image: The created image record.
        """
                
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
        """
        Deletes an image record from the database by the given `image_id`.
        
        If the image is found, it is deleted from the database and `True` is returned. If the image is not found, an `HTTPException` with a 404 status code is raised.
        
        Args:
            image_id (int): The ID of the image to be deleted.
        
        Returns:
            bool: `True` if the image was successfully deleted, `False` otherwise.
        
        Raises:
            HTTPException: If the image with the given `image_id` is not found in the database.
        """
        
        db_image = session.query(Image).filter(Image.id == image_id).first()
        
        if db_image:
            session.delete(db_image)
            session.commit()
            return True
        else:
            raise HTTPException(status_code=404, detail="Image not found")