from typing import List, Dict
from fastapi import WebSocket
from app.webSocket.broadcast_message import broadcast_message
from app.order.status_validator import is_valid_status_transition

async def update_order_status(orders: List[Dict], order_id: str, new_status: str, active_connections: List[WebSocket]) -> bool:
    """
    주문 상태 업데이트 && 결과 브로드캐스ㅌ팅
    """
    for order in orders:
        if order["order_id"] == str(order_id):
            if not is_valid_status_transition(order["status"], new_status):
                return False
            order["status"] = new_status
            await broadcast_message(active_connections, {
                "type": "status_update",
                "order_id": order_id,
                "status": new_status
            })
            return True
    return False