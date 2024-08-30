from fastapi import WebSocket
from typing import List


class ConnectionManager:
    """
    Manages a collection of active WebSocket connections.
    
    The `ConnectionManager` class provides methods to connect, disconnect, and broadcast messages to all active WebSocket connections.
    """
        
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """
        Accepts a new WebSocket connection and adds it to the list of active connections.
        
        Args:
            websocket (WebSocket): The WebSocket connection to be added to the list of active connections.
        """
                
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """
        Removes the specified WebSocket connection from the list of active connections.
        
        Args:
            websocket (WebSocket): The WebSocket connection to be removed from the list of active connections.
        """
                
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """
        Broadcasts the provided message to all active WebSocket connections.
        
        Args:
            message (str): The message to be sent to all active WebSocket connections.
        """
                
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

