# 10 Virtual Memory Management 03 - Replacement Strategies for Fixed allocation 01

### Locality

- 프로세스가 프로그램/데이터의 특정 영역을 집중적으로 참조하는 현상
- 원인
  - Loop structure in program
  - Array, structure 등의 데이터 구조
- 공간적 지역성(Spatial locality)
  - 참조한 영역과 인접한 영역을 참조하는 특성
- 시간적 지역성(Temporal locality)
  - 한 번 참조한 영역을 곧 다시 참조하는 특성



## Fixed allocation

### Min Algorithm (OPT algorithm)

- 1966년 Belady에 의해 제시
- Minimize page fault frequency(proved)
  - Optimal solution
- 기법
  - 앞으로 가장 오랫동안 참조되지 않을 page 교체
    - Tie-breaking rule : page 번호가 가장 큰 / 작은 페이지 교체
- 실현 불가능한 기법(Unrealizable)
  - Page reference string을 미리 알고 있어야 함
- 교체 기법의 성능 평가 도구로 사용됨



### Random Algorithm

- 무작위로 교체할 page 선택
- Low overhead
- No policy



### FIFO Algorithm

- First In First Out
  - 가장 오래된 page를 교체
- Page가 적재된 시간을 기억하고 있어야 함
- 자주 사용되는 page가 교체될 가능성이 높음
  - Locality에 대한 고려가 없음
- FIFO anomaly(Belady's anomaly)
  - FIFO 알고리즘의 경우, 더 많은 page frame을 할당받음에도 불구하고 page fault의 수가 증가하는 경우가 있음



### LRU(Least Recently Used) Algorithm

- 가장 오랫동안 참조되지 않은 page를 교체
- Page 참조시마다 시간을 기록해야 함
- Locality에 기반을 둔 교체 기법
- MIN algorithm에 근접한 성능을 보여줌
- 실제로 가장 많이 활용되는 기법
- 단점
  - 참조 시 마다 시간을 기록해야 함(Overhead)
    - 간소화된 정보 수집으로 해소 가능
      - 예) 정확한 시간 대신, 순서만 기록
  - Loop 실행에 필요한 크기보다 작은 수의 page frame이 할당된 경우, page fault 수가 급격히 증가함
    - 예) loop를 위한 |Ref.string| = 4 / 할당된 page frame이 3개
    - Allocation 기법에서 해결해야 함