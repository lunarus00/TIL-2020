# 07 Deadlock 02 - Deadlock model

## Graph Model

- Node
  - 프로세스 노드(P1, P2), 자원 노드(R1, R2)
- Edge
  - Rj -> Pi : 자원 Rj 이 프로세스 Pi에 할당됨
  - Pi -> Rj : 프로세스 Pi가 자원 Rj을 요청 (대기 중)



## State Transition Model

- 예제

  - 2개의 프로세스와 A type의 자원 2개(unit) 존재
  - 프로세스는 한번에 자원 하나만 요청/반납 가능

- State

  - | state | # of R units allocated | Request |
    | ----- | ---------------------- | ------- |
    | 0     | 0                      | X       |
    | 1     | 0                      | O       |
    | 2     | 1                      | X       |
    | 3     | 1                      | O       |
    | 4     | 2                      | X       |



## Deadlock 발생 필요 조건

- 자원의 특성
  - Exclusive use of resources
  - Non-preemptible resources
- 프로세스의 특성
  - Hold and wait(Partial allocation)
    - 자원을 하나 hold하고 다른 자원 요청
  - Circular wait
- 위 조건이 다 성립해야 Deadlokc이 발생한다

