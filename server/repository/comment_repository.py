from config.database import session
from repository.repository import AbstractRepository
from fastapi import HTTPException
from models.comments import Comment


class CommentRepository(AbstractRepository):  # inherits Abstractrepository
    """
    Provides a repository for managing comments related to tasks.

    The `CommentRepository` class inherits from the `AbstractRepository`
    class and provides methods for:
    - Retrieving comments for a given task ID
    - Adding a new comment for a task
    - Removing a comment for a task
    - Updating an existing comment for a task

    The repository uses the `session` object from the `config.database`
    module to interact with the database.
    """

    def get(self, task_id: int) -> list[Comment]:  # get logic
        """
        Retrieves all comments associated with the specified task ID.
        
        Args:
            task_id (int): The ID of the task to retrieve comments for.
        
        Returns:
            list[Comment]: A list of all `Comment` objects associated with
            the specified task ID.
        """
                
        details = session.query(Comment).filter(Comment.task_id == task_id).all()
        return details

    def add(self, comment: str, task_id: int, owner_id: int):
        """
        Adds a new comment for the specified task and owner.
        
        Args:
            comment (str): The text content of the new comment.
            task_id (int): The ID of the task the comment is associated with.
            owner_id (int): The ID of the user who is creating the comment.
        
        Returns:
            Comment: The newly created `Comment` object.
        
        Raises:
            HTTPException: If there is an error adding the comment to the 
            database.
        """
                
        new_comment_obj = Comment(comment=comment, task_id=task_id, owner_id=owner_id)
        try:
            session.add(new_comment_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=f"Unable to add comments: {e}")
        return new_comment_obj

    def remove(self, task_id: int, comment_id: int):
        """
        Removes a comment with the specified `comment_id` for the task with 
        the specified `task_id`.
        
        Args:
            task_id (int): The ID of the task the comment is associated with.
            comment_id (int): The ID of the comment to remove.
        
        Returns:
            Comment: The removed `Comment` object, or `None` if the 
            comment was not found.
        """
                
        remove_comment = (
            session.query(Comment)
            .filter(Comment.id == comment_id, Comment.task_id == task_id)
            .first()
        )
        if remove_comment:
            session.delete(remove_comment)
            session.commit()
        return remove_comment

    def update(self, task_id: int, comment_id: int, new_comment: str):
        """
        Updates the comment with the specified `comment_id` for the task 
        with the specified `task_id` with the new comment text.
        
        Args:
            task_id (int): The ID of the task the comment is associated with.
            comment_id (int): The ID of the comment to update.
            new_comment (str): The new text content for the comment.
        
        Returns:
            Comment: The updated `Comment` object, or `None` if the 
            comment was not found.
        """
                
        update_comment = (
            session.query(Comment)
            .filter(Comment.id == comment_id, Comment.task_id == task_id)
            .first()
        )
        if update_comment:
            update_comment.comment = new_comment
            session.commit()
        return update_comment
