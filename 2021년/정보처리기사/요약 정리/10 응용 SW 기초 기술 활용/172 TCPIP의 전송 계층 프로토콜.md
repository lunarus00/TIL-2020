# 172 TCP/IP의 전송 계층 프로토콜

## TCP(Transmission Control Protocol)

- 양방향 연결(Full Duplex Connection)형 서비스를 제공한다
- 가상 회선 연결(Virtual Circuit Connection) 형태의 서비스를 제공한다
- 스트림 위주의 전달(패킷 단위)을 한다
- 신뢰성 있는 경로를 확립하고 메시지 전송을 감독한다



## UDP(User Datagram Protocol)

- 데이터 전송 전에 연결을 설정하지 않는 비연결형 서비스를 제공한다
- TCP에 비해 상대적으로 단순한 헤더 구조를 가지므로, 오버헤드가 적다
- 고속의 안정성 있는 전송 매체를 사용하여 빠른 속도를 필요로 하는 경우, 동시에 여러 사용자에게 데이터를 전달할 경우, 정기적으로 반복해서 전송할 경우에 사용한다
- 실시간 전송에 유리하며, 신뢰성보다는 속도가 중요시되는 네트워크에서 사용된다



## RTCP(Real-Time Control Protocol)

- RTP(Real-time Transport Protocol) 패킷의 전송 품질을 제어하기 위한 제어 프로토콜이다
- 세션(Session)에 참여한 각 참여자들에게 주기적으로 제어 정보를 전송한다
- 하위 프로토콜은 데이터 패킷과 제어 패킷의 다중화(Multiplexing)를 제공한다