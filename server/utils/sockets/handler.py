import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from schemas.comment_payload import CreateCommentPayload
from service.comment_services import create_comment
from ..sockets.notification import get_greeting
from ..sockets.manager import manager

router = APIRouter()


@router.websocket("/ws/message")
async def websocket_endpoint(websocket: WebSocket):
    """
    Establishes a WebSocket connection and sends a greeting 
    message to the connected client.
    
    When a client connects to the WebSocket endpoint, this 
    function accepts the connection and sends a greeting message 
    to the client. It then enters a loop to receive text messages 
    from the client, but does not process them. When the client 
    disconnects, the function returns a message indicating the 
    client has disconnected.
    
    Args:
        websocket (WebSocket): The WebSocket connection object.
    
    Returns:
        str: A message indicating the client has disconnected.
    """
        
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
    """
    Handles the WebSocket connection for the comments endpoint.
    
    When a client connects to the WebSocket comments endpoint, 
    this function accepts the connection and adds the WebSocket 
    to the connection manager. It then enters a loop to receive 
    text messages from the client, parse the comment data, 
    create a new comment, and broadcast the new comment to all 
    connected clients.
    
    If the client disconnects, the function removes the WebSocket 
    from the connection manager.
    
    Args:
        websocket (WebSocket): The WebSocket connection object.
    
    Raises:
        WebSocketDisconnect: Raised when the client disconnects 
        from the WebSocket.
    """
        
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
