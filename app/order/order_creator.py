from typing import List, Dict
from fastapi import WebSocket
from datetime import datetime
from app.webSocket.broadcast_message import broadcast_message

async def create_order(order_data: dict, orders: List[Dict], active_connections: List[WebSocket]) -> dict:
    """
    신주문 생성 및 브로드캐스팅
    """
    new_order = {
        "order_id": str(len(orders) + 1),
        "item": order_data.get("item"),
        "quantity": order_data.get("quantity"),
        "status": "접수됨",
        "timestamp": datetime.now().isoformat()
    }
    
    orders.append(new_order)
    await broadcast_message(active_connections, {
        "type": "new_order",
        "order": new_order
    })
    
    return new_order