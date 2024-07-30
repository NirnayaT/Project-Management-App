from Database.database import Comment, session
from Database.enumeration import CommentStatus
from repository import AbstractRepository
from fastapi import HTTPException


class CommentRepository(AbstractRepository):  # inherits Abstractrepository

    def get(self, task_id: int) -> list[Comment]:  # get logic
        details = session.query(Comment).filter(Comment.task_id == task_id).all()
        return details

    def add(self, comment: str, task_id: int, user_id: int):
        new_comment_obj = Comment(comment=comment, task_id=task_id, user_id=user_id)
        try:
            session.add(new_comment_obj)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=f"Unable to add comments: {e}")
        return new_comment_obj

    def remove(self, task_id: int, comment_id: int):
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
        update_comment = (
            session.query(Comment)
            .filter(Comment.id == comment_id, Comment.task_id == task_id)
            .first()
        )
        if update_comment:
            update_comment.comment = new_comment
            session.commit()
        return update_comment
