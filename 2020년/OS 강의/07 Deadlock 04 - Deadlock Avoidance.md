# 07 Deadlock - Deadlock Avoidance

## Deadlock Avoidance(회피)

- 시스템의 상태를 계속 감시
- 시스템이 deadlock 상태가 될 가능성이 있는 자원 할당 요청시 요청을 보류
- 시스템을 항상 safe state로 유지



### Safe state

- 모든 프로세스가 정상적 종료 가능한 상태
- Safe sequence가 존재
  - Deadlock 상태가 되지 않을 수 있음을 보장



### Unsafe state

- Deadlock 상태가 될 가능성이 있음
- 반드시 발생한다는 의미는 아님



### 가정

- 프로세스의 수가 고정됨
- 자원의 종류와 수가 고정됨
- 프로세스가 요구하는 자원 및 최대 수량을 알고 있음
- 프로세스는 자원을 사용 후 반드시 반납한다
- Not practical 한 가정들임



### Dijkstra's algorithm

- Banker's algorithm
  - Deadlock avoidance를 위한 간단한 이론적 기법
  - 가정
    - 한 종류(resource type)의 자원이 여러 개(unit)
  - 시스템을 항상 safe state로 유지



### Habermann's algorithm

- Dijkstra's algorithm의 확장
- 여러 종류의 자원 고려
  - Multiple resource types
  - Multiple resource units for each resource type
- 시스템을 항상 safe state로 유지



## Deadlock Avoidance

- Deadlock의 발생을 막을 수 있음
- High overhead
  - 항상 시스템을 감시하고 있어야 한다
- Low resource utilization
  - Safe state 유지를 위해 사용되지 않는 자원이 존재
- Not practical
  - 가정
    - 프로세스 수, 자원 수가 고정
    - 필요한 최대 자원 수를 알고 있음