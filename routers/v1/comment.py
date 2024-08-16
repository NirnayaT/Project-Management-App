from fastapi import APIRouter
from service.comment_services import (
    display_comments,
    create_comment,
    remove_comment,
    update_comment as update_comment_route,
)
from schemas.comment_payload import (
    CreateCommentPayload,
    RemoveCommentPayload,
    UpdateCommentPayload,
)
from fastapi import Depends

from models.users import User
from utils.auth.jwt_handler import get_current_user

# from Users.auth.dependencies import get_current_user


router = APIRouter(
    tags=["Comment Management"]
)


@router.post("/comments/add")
async def add_comment(comment: CreateCommentPayload, current_user: User = Depends(get_current_user)):
    return await create_comment(comment, current_user.id)


@router.get("/comments/show")
async def show_comments(task_id, current_user: User = Depends(get_current_user)):
    return await display_comments(task_id)


@router.delete("/comments/remove")
async def delete_comment(payload: RemoveCommentPayload, current_user: User = Depends(get_current_user)):
    return await remove_comment(payload), await display_comments(payload.task_id)


@router.put("/comments/update")
async def update_comment(payload: UpdateCommentPayload, current_user: User = Depends(get_current_user)):
    return await update_comment_route(payload), await display_comments(payload.task_id)
