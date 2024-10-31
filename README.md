# 기능 구현

- 클라이언트와의 CORS-sign 해결을 위한 미들웨어를 등록합니다.
- 클라이언트에서 요청과 함께 전달받은 본문을 메모리 내의 임시 저장소 (List)에 캐싱합니다.
- 클라이언트에서 주문 상태를 업데이트했을 때 이에 대한 정적인 값을 비교하고 유효하다면 상태를 변경합니다.
- 클라이언트에서의 추가적인 주문, 주문 상태 업데이트와 같은 상호작용이 일어났을 때 이를 저장하거나 업데이트합니다.
- 클라이언트에서 주문이 추가되거나 상태가 변경되면 웹 소켓을 통해 orders 즉,
  저장된 데이터의 모든 최신 정보를 브로드캐스트하여 실시간으로 정보를 전달합니다.
- put 요청에 대한 응답으로 주문 번호를 이용해 주문 현황으로 저장된 특정 데이터의 상태를 업데이트하고 이를 실시간으로 반영합니다.
- get 요청의 orders 엔드 포인트를 url에 입력해 실시간 주문 현황을 원본 형태의 객체로 반환받을 수 있습니다.

### 플로우 차트
![Untitled diagram-2024-10-31-003056](https://github.com/user-attachments/assets/aad641e6-da00-40f9-a580-070b74afdb1b)
