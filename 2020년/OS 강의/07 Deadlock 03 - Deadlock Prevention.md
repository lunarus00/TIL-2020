# 07 Deadlock 03 - Deadlock Prevention

- 4개의 Deadlock 발생 필요 조건 중 하나를 제거
  - Exclusive use of resources
  - Non-preemptible resources
  - Hold and wait (Partial allocation)
  - Circular wait
- Deadlock이 절대 발생하지 않음



### 모든 자원을 공유 허용

- Exclusive use of resources 조건 제거
- 현실적으로 불가능



### 모든 자원에 대해 선점 허용

- Non-preemptible resources 조건 제거
- 현실적으로 불가능
- 유사한 방법
  - 프로세스가 할당받을 수 없는 자원을 요청한 경우, 기존에 가지고 있던 자원을 모두 반납하고 작업 취소
    - 이후 처음 (또는 check-point) 부터 다시 시작
  - 심각한 자원 낭비 발생 -> 비현실적



### 필요 자원을 한번에 모두 할당(Total allocation)

- Hold and wait 조건 제거
- 자원 낭비 발생
  - 필요하지 않은 순간에도 가지고 있음
- 무한 대기 현상 발생 가능



### Circular wait 조건 제거

- Totally allocation을 일반화한 방법
- 자원들에게 순서를 부여
- 프로세스는 순서의 즈으가 방향으로만 자원 요청 가능
- 자원 낭비 발생



## Deadlock Prevention(예방)

- 4개의 Deadlock 발생 필요 조건 중 하나를 제거
- Deadlock이 절대 발생하지 않음
- 심각한 자원 낭비 발생
  - Low device utilization
  - Reduced system throughput
- 비현실적