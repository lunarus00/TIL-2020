# 06 프로세스 동기화와 상호배제 06 - Eventcount, Sequencer

## Sequencer

- 정수형 변수
- 생성시 0으로 초기화, 감소하지 않음
- 발생 사건들의 순서 유지
- ticket() 연산으로만 접근 가능

#### ticket(S)

- 현재까지 ticket() 연산이 호출된 횟수를 반환
- Indivisible operation



## Eventcount

- 정수형 변수
- 생성시 0으로 초기화, 감소하지 않음
- 특정 사건의 발생 횟수를 기록
- read(E), advance(E), await(E, v) 연산으로만 접근 가능

#### read(E)

- 현재 Eventcount 값 반환

#### advance(E)

- E <- E + 1
- E를 기다리고 있는 프로세스를 깨움(wake-up)

#### await(E, v)

- V는 정수형 변수
- if (E < v) 이면 E에 연결된 Qe에 프로세스 전달(push) 및 CPU scheduler 호출



- No busy waiting
- No starvation
  - FIFO scheduling for Qe
- Semaphore보다 더 low-level control이 가능