# 12 - 02 Disk Scheduling

## Disk Scheduling

- Disk access 요청들의 처리 순서를 결정
- Disk system의 성능을 향상
- 평가 기준
  - Throughput
    - 단위 시간당 처리량
  - Mean response time
    - 평균 응답 시간
  - Predictability
    - 응답 시간의 예측성
    - 요청이 무기한 연기(starvation)되지 않도록 방지



## Optimizing seek time

### FCFS(First Come First Service)

- 요청이 도착한 순성 따라 처리
- 장점
  - Simple
    - Low scheduling overhead
  - 공평한 처리 기법(무한 대기 방지)
- 단점
  - 최적 성능 달성에 대한 고려가 없음
- Disk access 부하가 적은 경우에 적합



### SSTF(Shortest Seek Time First)

- 현재 head 위치에서 가장 가까운 요청 먼저 처리
- 장점
  - Throughput 높음
  - 평균 응답 시간 단축
- 단점
  - Predictability 낮음
  - Starvation 현상 발생 가능
- 일괄처리 시스템에 적합함



### Scan Scheduling

- 현재 head의 진행 방향에서 head와 가장 가까운 요청 먼저 처리
- (진행 방향 기준) 마지막 cylinder 도착 후 반대 방향으로 진행
- 장점
  - SSTF의 starvation 문제 해결
  - Throughput 및 평균 응답시간 우수
- 단점
  - 진행 방향 반대쪽 끝 요청들의 응답시간이 길어짐



### C-Scan Scheduling

- Scan과 유사
- Head가 미리 정해진 방향으로만 이동
  - 마지막 cylinder 도착 후 시작 cylinder로 이동 후 재시작
- 장점
  - Scan 대비 균등한 기회 제공
- 단점
  - 시작 cylinder로 불필요한 head 이동이 추가됨



### Look Scheduling

- Elevator algorithm
- Scan(C-Scan)에서 현재 진행 방향에 요청이 없으면 방향 전환
  - 마지막 cylinder까지 이동하지 않음
  - Scan(C-Scan)의 실제 구현 방법
- 장점
  - Scan의 불필요한 head 이동 제거



### Shortest Latency Time First(SLTF)

- Fixed head disk 시스템에 사용
  - 각 track마다 head를 가진 disk
  - Head의 이동이 없음
- Sector queuing algorithm
  - 각 sector별  queue 유지
  - Head 아래 도착한 sector의 queue에 있는 요청들을 먼저 처리함
- Moving head disk의 경우
  - 같은 cylinder 또는 track에 여러 개의 요청 처리를 위해 사용 가능
  - Head가 특정 cylinder에 도착하면 고정 후 해당 cylinder의 요청을 모두 처리



### Shortest Positioning Time First(SPTF)

- Positioning time = Seek time + rotational dealy
- Positioning time이 가장 작은 요청 먼저 처리
- 장점
  - Throughput 높음
  - 평균 응답 시간 빠름
- 단점
  - 가장 안쪽과 바깥쪽 cylinder의 요청에 대해 starvation 현상 발생 가능
- Eschenbach scheduling
  - Positioning time 최적화 시도
  - Disk가 1회전 하는 동안 요청을 처리할 수 있도록 요청을 정렬
    - 한 cylinder 내 track, sector들에 대한 다수의 요청이 있는 경우 다음 회전에 처리됨