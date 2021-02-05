# 06 프로세스 동기화와 상호배제 04 - Spinlock

## Spinlock

- 정수 변수
- 초기화, P(), V() 연산으로만 접근 가능
  - 위 연산들은 indivisible (or atomic) 연산
    - OS support
    - 전체가 한 instruction cycle에 수행됨

- 멀티 프로세서 시스템에서만 사용 가능
- Busy waiting