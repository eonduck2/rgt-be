from fastapi import WebSocket, WebSocketDisconnect
from typing import List, Dict
import json
from app.order.status_updater import update_order_status

async def handle_websocket_connection(
    websocket: WebSocket,
    active_connections: List[WebSocket],
    orders: List[Dict]
):
    """
    웹소켓 연결을 처리하고 메시지를 관리합니다.
    """
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        await websocket.send_json({
            "type": "orders_list",
            "orders": orders
        })
        
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            if message["type"] == "status_update":
                success = await update_order_status(
                    orders,
                    message["order_id"],
                    message["status"],
                    active_connections
                )
                
                if not success:
                    for order in orders:
                        if order["order_id"] == str(message["order_id"]):
                            await websocket.send_json({
                                "type": "status_update",
                                "order_id": message["order_id"],
                                "status": order["status"]
                            })
                            break
                            
    except WebSocketDisconnect:
        active_connections.remove(websocket)