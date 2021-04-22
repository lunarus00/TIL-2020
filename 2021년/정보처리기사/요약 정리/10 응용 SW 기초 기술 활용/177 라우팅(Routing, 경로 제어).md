# 177 라우팅(Routing, 경로 제어)

- 송수신 측 간의 전송 경로 중에서 최적 패킷 교환 경로를 결정하는 기능이다
- 경로 제어표(Routing Table)를 참조해서 이루어지며, 라우터에 의해 수행된다



### 라우팅 프로토콜

- RIP(Routing Information Protocol)
  - 현재 가장 널리 사용되는 라우팅 프로토콜로, 소규모 동종의 네트워크 내에서 효율적인 방법이며, 최대 흡수를 15로 제한함
- IGRP(Interior Gateway Routing Protocol)
  - RIP의 단점을 보완하기 위해 개발된 것으로, 네트워크 상태를 고려하여 라우팅하며, 중규모 네트워크에 적합함
- OSPF(Open Shortest Path First Protocol)
  - 대규모 네트워크에서 많이 사용되는 라우팅 프로토콜로, 라우팅 정보에 변화가 생길 경우 변화된 정보만 네트워크 내의 모든 라우터에 알리며, RIP에 비해 흡수에 제한이 없음
- BGP(Border Gateway Protocol)
  - 자율 시스템(AS) 간의 라우팅 프로토콜로, EGP의 단점을 보완하기 위해 개발되었음



### 라우팅 알고리즘

- 거리 벡터 알고리즘(Distance Vector Algorithm)
  - 인접해 있는 라우터 간의 거리(Distance)와 방향(Vector)에 대한 정보를 이용하여 최적의 경로를 찾고 그 최적 경로를 이용할 수 없을 경우 다른 경로를 찾는 알고리즘으로, RIP와 IGRP가 있음
- 링크 상태 알고리즘(Link State Algorithm)
  - 라우터와 라우터 간의 모든 경로를 파악하여 미리 대체 경로를 마련해 두는 알고리즘으로, 거리 벡터 알고리즘의 단점을 보완하기 위해 개발되었으며, OSPF가 있음