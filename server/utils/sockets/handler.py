import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from schemas.comment_payload import CreateCommentPayload
from service.comment_services import create_comment
from ..sockets.notification import get_greeting
from ..sockets.manager import manager

router = APIRouter()


@router.websocket("/ws/message")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    greeting = get_greeting()
    await websocket.send_text(greeting)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect as e:
        return f"Client disconnected: {e}"

@router.websocket("/ws/comments")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            comment_data = json.loads(data)
            payload = CreateCommentPayload(**comment_data)
    
            new_comment = await create_comment(payload)


            await manager.broadcast(f"New comment added: {new_comment.comment}")
            # await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
