# 08 Memory Management 03 - Variable Partition Multi-programming

## Variable Partition Multiprogramming

- 초기에는 전체가 하나의 영역
- 프로세스를 처리하는 과정에서 메모리 공간이 동적으로 분할
- No internal fragmentation



## 배치 전략(Placement strategies)

### First-fit (최초 적합)

- 충분한 크기를 가진 첫 번째 partition을 선택
- Simple and low overhead
- 공간 활용률이 떨어질 수 있음



### Best-fit (최적 적합)

- Process가 들어갈 수 있는 partition 중 가장 작은 곳 선택
- 탐색시간이 오래 걸림
  - 모든 partition을 살펴봐야 함
- 크기가 큰 partition을 유지할 수 있음
- 작은 크기의 partition이 많이 발생
  - 활용하기엔 너무 작은 크기의 partition 이 발생함



### Worst-fit (최악 적합)

- Process가 들어갈 수 있는 partition 중 가장 큰 곳 선택
- 탐색시간이 오래 걸림
  - 모든 partition을 살펴봐야 함
- 작은 크기의 partition 발생을 줄일 수 있음
- 큰 크기의 partition 확보가 어려움
  - 큰 프로세스에게 필요한 크기의 partition 확보의 어려움



### Next-fit (순차 최초 적합)

- 최초 적합 전략과 유사
- State table에서 마지막으로 탐색한 위치부터 탐색
- 메모리 영역의 사용 빈도 균등화
- Low overhead



### External fragmentation issue 발생 시

#### Coalescing holes(공간 통합)

- 인접한 빈 영역을 하나의 partition으로 통합
  - Process가 memory를 release하고 나가면 수행
  - Low overhead

#### Storage Compaction(메모리 압축)

- 모든 빈 공간을 하나로 통합
- 프로세스 수행에 필요한 적재 공간 확보가 필요할 때 수행
- High overhead
  - 모든 Process 재배치(Process 들이 중지된 후 재배치 됨)
  - 많은 시스템 자원을 소비