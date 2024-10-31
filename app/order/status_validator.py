def is_valid_status_transition(current_status: str, new_status: str) -> bool:
    """
    주문 상태 변경이 유효한지 검사
    """
    valid_transitions = {
        "접수됨": ["처리중"],
        "처리중": ["완료"],
        "완료": []
    }
    return new_status in valid_transitions.get(current_status, [])