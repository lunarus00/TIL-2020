# 06 프로세스 동기화와 상호배제 05 - Semaphore

## Semaphore

- 1965년 Dijkstra가 제안
- Busy waiting 문제 해결
- 음이 아닌 정수형 변수(s)
  - 초기화 연산, P(), V()로만 접근 가능
    - P : Probern(검사)
    - V : Verhogen(증ㅇ가)
- 임의의 s변수 하나에 ready queue 하나가 할당됨



#### Binary semaphore

- S가 0과 1 두 종류의 값만 갖는 경우
- 상호배제나 프로세스 동기화의 목적으로 사용

#### Counting semaphore

- S가 0 이상의 정수값을 가질 수 있는 경우
- Producer-Consumer 문제 등을 해결하기 위해 사용
  - 생산자-소비자 문제



- 초기화 연산

  - S 변수에 초기값을 부여하는 연산

- P() 연산, V() 연산

  - P(S) 연산

    - ```
      if (S > 0)
      	then S <- S - 1;
      else wait on the queue Qs;
      ```

  - V(S) 연산

    - ```
      if (∃ waiting process on Qs)
      	then wakeup one of them;
      else S <- S + 1;
      ```

- 모두 indivisible 연산

  - OS support
  - 전체가 한 instruction cycle에 수행됨



#### Semaphore로 해결 가능한 동기화 문제들

- 상호배제 문제
  - Mutual exclusion
- 프로세스 동기화 문제
  - process synchronization problem
- 생산자-소비자 문제
  - producer-consumer problem
- Reader-Writher 문제
- Dining philosopher problem
- 기타



#### Process synchronization

- Process들의 실행 순서 맞추기
  - 프로세스들은 병행적이며, 비동기적으로 수행

#### Producer-Consumer problem

- 생산자(Producer) 프로세스
  - 메시지를 생성하는 프로세스 그룹
- 소비자(Consumer) 프로세스
  - 메세지 전달받는 프로세스 그룹

#### Reader-Writer problem

- Reader
  - 데이터에 대해 읽기 연산만 수행
- Writer
  - 데이터에 대해 갱신 연산을 수행
- 데이터 무결성 보장 필요
  - Reader들은 동시에 데이터 접근 가능
  - Writer들(또는 reader와 writer)이 동시 데이터 접근 시, 상호배제(동기화) 필요
- 해결법
  - reader / writer에 대한 우선권 부여
    - reader preference solution
    - writer preference solution



- No busy waiting
  - 기다려야 하는 프로세스는 block(asleep) 상태가 됨
- Semaphore queue에 대한 wake-up 순서는 비결정적
  - Starvation problem