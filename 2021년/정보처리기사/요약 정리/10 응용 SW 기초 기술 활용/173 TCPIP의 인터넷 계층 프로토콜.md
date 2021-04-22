# 173 TCP/IP의 인터넷 계층 프로토콜

- IP(Internet Protocol) : 전송할 데이터에 주소 지정 및 경로 설정 등의 기능을 하며, 비연결형인 데이터그램 방식을 사용하므로 신뢰성이 보장되지 않음
- ICMP(Internet Control Message Protocol) : IP와 조합하여 통신중에 발생하는 오류의 처리와 전송 경로 변경 등을 위한 제어 메시지를 관리하는 역할을 하며, 헤더는 8Byte로 구성됨
- IGMP(Internet Group Management Protocol) : 멀티캐스트를 지원하는 호스트나 라우터 사이에서 멀티캐스트 그룹 유지를 위해 사용됨
- ARP(Address Resolution Protocol) : 호스트의 IP 주소를 호스트와 연결된 네트워크 접속 장치의 물리적 주소(MAC Address)로 바꿈
- RARP(Reverse Addredd Resolution Protocol) : ARP와 반대로 물리적 주소를 IP 주소로 변환하는 기능을 함