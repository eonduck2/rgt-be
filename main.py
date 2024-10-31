from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

from app.handler.websocket_handler import handle_websocket_connection
from app.order.order_creator import create_order
from app.order.status_updater import update_order_status

app = FastAPI()

# CORS 설정 (미들우 ㅔ어 등록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 전역 상태 저장소
orders: List[Dict] = []
active_connections: List[WebSocket] = []

# WebSocket 연결 처리 및 실시간 통신 설정
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await handle_websocket_connection(websocket, active_connections, orders)

# 새로운 주문을 생성하고 저장
@app.post("/order")
async def create_order_endpoint(order_data: dict):
    new_order = await create_order(order_data, orders, active_connections)
    return {
        "message": "주문이 접수되었습니다",
        "order": new_order
    }

# 특정 주문의 상태를 업데이트
@app.put("/order/{order_id}/status")
async def update_order_status_endpoint(order_id: str, new_status: dict):
    success = await update_order_status(
        orders,
        order_id,
        new_status.get("status"),
        active_connections
    )
    
    if success:
        return {"message": "주문 상태가 업데이트되었습니다"}
    return {"message": "주문을 찾을 수 없거나 잘못된 상태 변경입니다"}

# 저장된 모든 주문 목록을 조회 (따로 요청 잡아둔 거 없어서 경로 직접 쳐서 봐야)
@app.get("/orders")
async def get_orders():
    return orders