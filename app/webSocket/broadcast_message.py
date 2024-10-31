from fastapi import WebSocket
from typing import List

async def broadcast_message(active_connections: List[WebSocket], message: dict):
    """
    모든 활성 웹소켓 연결에 메시지를 전송
    """
    for connection in active_connections:
        await connection.send_json(message)