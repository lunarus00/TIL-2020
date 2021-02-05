# 07 Deadlock 05 - Deadlock Detection and Recovery

## Deadlock Detection(검출)

- Deadlock 방지를 위한 사전 작업을 하지 않음
  - Deadlock이 발생 가능
- 주기적으로 deadlock 발생 확인
  - 시스템이 deadlock 상태인가?
  - 어떤 프로세스가 deadlock 상태인가?
- Resource Allocation Graph(RAG) 사용
  - Deadlock 검출을 위해 사용
  - Directed, bipartite Graph



### Graph reduction

- 주어진 RAG에서 edge를 하나씩 지워가는 방법
- Completely reduced
  - 모든 edge가 제거됨
  - Deadlock에 빠진 프로세스가 없음
- Irreducible
  - 지울 수 없는 edge가 존재
  - 하나 이상의 프로세스가 deadlock 상태
- Unblocked process
  - 필요한 자원을 모두 할당 받을 수 있는 프로세스



## Deadlock Detection Method

### Graph reduction procedure

1. Unblocked process에 연결된 모든 edge를 제거
2. 더이상 unblocked process가 없을 때까지 1 을 반복

- 최종 Graph에서
  - 모든 edge가 제거됨(Completely reduced)
    - 현재 상태에서 deadlock이 없음
  - 일부 edge가 남음(irreducible)
    - 현재 deadlock이 존재



### Graph Reduction

- High overhead
  - 검사 주기에 영향을 받음
  - Node의 수가 많은 경우
- Low overhead deadlock detection methods(Special case)
  - Case-1) Single-unit resources
    - Cycle detection
  - Case-2) Single-unit request in expedient state
    - Knot detection



## Deadlock Avoidance(회피) vs Detection(탐지)

### Deadlock avoidance

- 최악의 경우를 생각
  - 앞으로 일어날 일을 고려
- Deadlock이 발생하지 않음



### Deadlock detection

- 최선의 경우를 생각
  - 현재 상태만 고려
- Deadlock 발생 시 Recovery 과정이 필요



## Deadlock Recovery

- Deadlock을 검출한 후 해결하는 과정
- Deadlock recovery methods
  - Process termination
    - Deadlock 상태에 있는 프로세스를 종료시킴
    - 강제 종료된 프로세스는 이후 재시작 됨
  - Resource preemption
    - Deadlock 상태 해결을 위해 선점할 자원을 선택
    - 선정된 자원을 가지고 있는 프로세스에서 자원을 빼앗음
      - 자원을 빼앗긴 프로세스는 강제 종료됨



### Process termination

- Deadlock 상태인 프로세스 중 일부 종료
- Termination cost model
  - 종료시킬 deadlock 상태의 프로세스 선택
  - Termination cost
    - 우선순위 / Process priority
    - 종류 / Process type
    - 총 수행 시간 / Accumulated execution time of the process
    - 남은 수행 시간 / Remaining time of the process
    - 종료 비용 / Accounting cost
    - Etc
- 종료 프로세스 선택
  - Lowest-termination cost process first
    - Simple
    - Low overhead
    - 불필요한 프로세스들이 종료될 가능성이 높음
  - Minimum cost recovery
    - 최소 비용으로 deadlock 상태를 해소할 수 있는 process 선택
      - 모든 경우의 수를 고려해야 함
    - Complex
    - High overhead
      - O(2ⁿ)



### Resource preemption

- Deadlock 상태 해결을 위해 선점할 자원 선택
- 해당 자원을 가지고 있는 프로세스를 종료시킴
  - Deadlock 상태가 아닌 프로세스가 종료될 수도 있음
  - 해당 프로세스는 이후 재시작 됨
- 선점할 자원 선택
  - Preemption cost model이 필요
  - Minimum cost recovery method 사용
    - O(r)



### Checkpoint-restart method

- 프로세스의 수행 중 특정 지점(checkpoint)마다 context를 저장
- Rollback을 위해 사용
  - 프로세스 강제 종료 후, 가장 최근의 checkpoint에서 재시작