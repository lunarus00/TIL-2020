# 10 Virtual Memory Management 05 - Replacement Strategies for Variable Allocation

## Variable Allocation

### Working Set (WS) algorithm

- 1968년 Denning이 제안
- Working set
  - Process가 특정 시점에 자주 참조하는 page들의 집합
  - 최근 일정 시간 동안(Δ) 참조된  page들의 집합
  - 시간에 따라 변함
  - W(t, Δ)
    - The working set of a process at time t
    - Time interval [t-Δ, t] 동안 참조된 pages들의 집합
    - Δ : window size, system parameter
- Working set memory management
  - Locality에 기반을 둠
  - Working set을 메모리에 항상 유지
    - Page fault rate(thrashing) 감소
    - 시스템 성능 향상
  - Window size(Δ)는 고정
    - Memory allocation은 가변
      - MA가 고정 and Δ가 가변 = LRU algorithm
    - Δ 값이 성능을 결정짓는 중요한 요소
- 성능 평가
  - Page fault 수 외의 다른 지표도 함께 봐야 함
  - Example
    - Time interval [1, 10]
      - `# of page fault = 5`
      - 평균 할당 page frame 수 = 3.2
    - 평가
      - 평균 3.2개의 page frame을 할당받은 상태에서 5번의 page fault 발생
- 특성
  - 적재되는 page가 없더라도 메모리를 반납하는 page가 있을 수 있음
  - 새로 적재되는 page가 있더라도 교체되는 page가 없을 수 있음
- 단점
  - Working set management overhead
  - Residence set(상주 집합)을 Page fault가 없더라도 지속적으로 관리해야 함



### Page Fault Frequency(PFF) algorithm

- Residence set size를 page fault rate에 따라 결정
  - Low page fault rate(long inter-fault time)
    - Process에게 할당된 PF 수를 감소
  - High page fault rate(short inter-fault time)
    - Process에게 할당된 PF 수를 증가
- Resident set 갱신 및 메모리 할당
  - Page fault가 발생시에만 수행
  - Low overhead
- Criteria for page fault rate
  - IFT > τ : Low page fault rate
  - IFT < τ : High page fault rate
  - τ : threshold value
    - System parameter
- Algorithm
  1. Page fault 발생 시 IFT 계산
     - IFT = tc - t(c-1)
       - t(c-1) : time of previous page fault
       - tc : time of current page fault
  2. IFT > τ (Low page fault rate)
     - Residence set <- [t(c-1), tc] 동안 참조된 page들만 유지
     - 나머지 page들은 메모리에서 내림
       - 메모리 할당(# of page frames) 유지 or 감소
  3. IFT <= τ (High page fault rate)
     - 기존 page들 유지
     - 현재 참조된 page를 추가 적재
       + 메모리 할당(# of page frames) 증가



### Variable MIN (VMIN) algorithm

- Variable allocation 기반 교체 기법 중 optimal algorithm
  - 평균 메모리 할당량과 page fault 발생 횟수를 모두 고려했을 때의 Optimal
- 실현 불가능한 기법 (Unrealizable)
  - Page reference string을 미리 알고 있어야 함
- 기법
  - [t, t + Δ] 을 고려해서 교체할 page 선택
- Algorithm
  - Page r이 t 시간에 참조되면 page r이 [t, t+Δ] 사이에 다시 참조되는지 확인
  - 참조된다면 page r을 유지
  - 참조되지 않으면 page r을 메모리에서 내림
- 성능 평가
  - Page fault 수 외 다른 지표도 함께 봐야 함
  - Example
    - Time interval [1, 10]
      - `# of page fault = 5`
      - 평균 할당 page frame 수 = 1.6
    - 평가
      - 평균 1.6개의 page frame을 할당받은 상태에서 5번의 page fault 발생
- 최적 성능을 위한 Δ 값은?
  - Δ = R / U
    - U : 한번의 참조시간 동안 page를 메모리에 유지하는 비용
    - R : page fault 발생 시 처리 비용
  - R > Δ * U (Δ가 작으면)
    - page fault 처리 비용 > page 유지 비용
  - R < Δ * U (Δ가 크면)
    - page fault 처리 비용 < page 유지 비용

