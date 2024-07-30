from fastapi import APIRouter
from Comments.services import (
    display_comments,
    create_comment,
    remove_comment,
    update_comment as update_comment_route,
)
from Comments.payload import (
    CreateCommentPayload,
    RemoveCommentPayload,
    UpdateCommentPayload,
)
from fastapi import Depends
from Users.auth.jwt_bearer import jwtBearer

router = APIRouter()


@router.post("/comments/add", dependencies=[Depends(jwtBearer())])
def add_comment(comment: CreateCommentPayload):
    return create_comment(comment)


@router.get("/comments/show", dependencies=[Depends(jwtBearer())])
def show_comments(task_id):
    return display_comments(task_id)


@router.delete("/comments/remove", dependencies=[Depends(jwtBearer())])
def delete_comment(payload: RemoveCommentPayload):
    return remove_comment(payload), display_comments(payload.task_id)


@router.put("/comments/update", dependencies=[Depends(jwtBearer())])
def update_comment(payload: UpdateCommentPayload):
    return update_comment_route(payload), display_comments(payload.task_id)
