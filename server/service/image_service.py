import base64
import os
from pathlib import Path
from uuid import uuid4
from fastapi import HTTPException, UploadFile
from repository.image_repository import ImageRepository
from schemas.image import ImageCreate
from config.database import session
from models.images import Image
from models.users import User


MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


def save_image(file: UploadFile, user_id: int):
    """
    Saves a new image uploaded by the user.
    
    Args:
        file (UploadFile): The uploaded file object.
        user_id (int): The ID of the user uploading the image.
    
    Raises:
        HTTPException: If the user has already uploaded an image, the file size exceeds the maximum allowed size, or the file format is unsupported.
    
    Returns:
        The created image data.
    """
        
    
    existing_image = session.query(Image).filter(Image.user_id == user_id).first()
    
    if existing_image:
        raise HTTPException(status_code=400, detail="User has already uploaded an image.")

    upload_directory = "images"
    os.makedirs(upload_directory, exist_ok=True)

    file_size = len(file.file.read())
    file.file.seek(0)

    if file_size > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds the maximum allowed size of 250 KB.",
        )

    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in ["jpg", "jpeg", "png"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Only JPG, JPEG, and PNG are allowed.",
        )

    unique_filename = f"{uuid4()}.{file_extension}"
    file_location = os.path.join(upload_directory, unique_filename)

    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())

    image_data = ImageCreate(
        filename=unique_filename,
        path=file_location,
        url=f"/static/images/{unique_filename}",
        user_id=user_id,
    )

    image_repo = ImageRepository()
    return image_repo.add(image_data)


def image_to_base64(current_user):
    """
    Converts the image associated with the current user to a base64-encoded string.
    
    Returns:
        str: The base64-encoded image data, or raises an HTTPException if the image is not found or the image file is not accessible.
    """
        
    image = session.query(Image).filter(Image.user_id == current_user.id).first()

    if image:
        image_path = Path(image.path)
        if not image_path.is_file():
            raise HTTPException(
                status_code=404, detail="Image file not found on the server"
            )

        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")

        return base64_image

    # else:
    #     raise HTTPException(
    #         status_code=404, detail="Image not found for the current user"
    #     )
    
        
def update_image(file: UploadFile, user_id: int):
    """
    Updates an existing image for the current user.
    
    Args:
        file (UploadFile): The new image file to be uploaded.
        user_id (int): The ID of the user whose image is being updated.
    
    Raises:
        HTTPException(404): If no image is found for the current user.
        HTTPException(500): If there is a failure deleting the old image file.
        HTTPException(400): If the new file size exceeds the maximum allowed size or the file format is not supported.
        HTTPException(500): If there is a failure saving the new image file.
    
    Returns:
        Image: The newly created image record.
    """
        

    existing_image = session.query(Image).filter(Image.user_id == user_id).first()

    if not existing_image:
        raise HTTPException(status_code=404, detail="No image found to update.")

    # Remove the existing image file from the filesystem
    existing_image_path = Path(existing_image.path)
    if existing_image_path.is_file():
        try:
            os.remove(existing_image_path)
        except OSError:
            raise HTTPException(status_code=500, detail="Failed to delete old image file.")
    
    # Remove the existing image record from the database
    image_repo = ImageRepository()
    image_repo.remove(existing_image.id)

    # Handle the new image upload
    upload_directory = "images"
    os.makedirs(upload_directory, exist_ok=True)

    file_content = file.file.read()
    file_size = len(file_content)
    file.file.seek(0)

    if file_size > MAX_FILE_SIZE_BYTES:
        raise HTTPException(status_code=400, detail="File size exceeds the maximum allowed size of 5 MB.")
    
    # Validate file extension
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in ["jpg", "jpeg", "png"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Only JPG, JPEG, and PNG are allowed.",
        )

    unique_filename = f"{uuid4()}.{file_extension}"
    file_location = os.path.join(upload_directory, unique_filename)

    try:
        with open(file_location, "wb") as buffer:
            buffer.write(file_content)
    except IOError:
        raise HTTPException(status_code=500, detail="Failed to save new image file.")
    
    # Prepare the new image data
    image_data = ImageCreate(
        filename=unique_filename,
        path=file_location,
        url=f"/static/images/{unique_filename}",
        user_id=user_id,
    )
    
    # Save the new image in the database
    new_image = image_repo.add(image_data)
    
    return new_image

def get_user_by_email(email: str):
    """
    Retrieves a user by their email address.
    
    Args:
        email (str): The email address of the user to retrieve.
    
    Returns:
        User: The user object if found, otherwise raises an HTTPException with a 404 status code.
    
    Raises:
        HTTPException: If the user is not found, with a 404 status code.
    """
        
    user = session.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user