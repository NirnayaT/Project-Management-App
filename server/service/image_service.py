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
    return image_repo.create_image(image_data)


def image_to_base64(current_user):
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

    else:
        raise HTTPException(
            status_code=404, detail="Image not found for the current user"
        )
        
def update_image(file: UploadFile, user_id: int):
    # Find the existing image for the user
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
    image_repo.delete_image(existing_image.id)

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
    new_image = image_repo.create_image(image_data)
    
    return new_image

def get_user_by_email(email: str):
    user = session.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user