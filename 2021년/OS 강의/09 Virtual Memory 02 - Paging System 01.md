# 09 Virtual Memory 02 - Paging System 01

## Paging System

- 프로그램을 같은 크기의 블록으로 분할(Pages)
- Terminologies
  - Page
    - 프로그램의 분할된 block
  - Page frame
    - 메모리의 분할 영역
    - Page와 같은 크기로 분할
- 특징
  - 논리적 분할이 아님(크기에 따른 분할)
    - Page 공유(sharing) 및 보호(protection) 과정이 복잡함
      - Segmentation 대비
  - Simple and Efficient
    - Segmentation 대비
  - No external fragmentation
    - Internal fragmentation 발생 가능



### Address Mapping

- Virtual address : v = (p, d)
  - P : page number
  - d : displacement(offset)
- Address mapping
  - PMT(Page Map Table) 사용
- Address mapping mechanism
  - Direct Mapping(직접 사상)
  - Associative mapping(연관 사상)
    - TLB(Translation Look-aside Buffer)
  - Hybrid direct / associative mapping



#### Direct Mapping

- Block mapping 방법과 유사
- 가정
  - PMT를 커널 안에 저장
  - PMT entry size = entrySize
  - Page size = pageSize

1. 해당 프로세스의 PMT가 저장되어 있는 주소 b에 접근
2. 해당 PMT에서 page p에 대한 entry를 찾음
   - p의 entry 위치 = b + p * entrySize
3. 찾아진 entry의 존재 비트 검사
   1. Residence bit = 0 인 경우 `(page fault)`, swap device에서 해당 page를 메모리로 적재, PMT를 갱신한 후 3-2 단계 수행
      - page fault : Context switching 발생 (I / O) -> Overhead가 크다
   2. Residence bit = 1 인 경우, 해당 entry에서 page frame 번호 p' 를 확인
4. p' 와 가상 주소의 변위 d를 사용하여 실제 주소 r 형성
   - r = p' * pageSize + d
5. 실제 주소 r로 주기억장치에 접근

- 문제점
  - 메모리 접근 횟수 2배
    - 성능 저하(performance degradation)
  - PMT를 위한 메모리 공간 필요
- 해결방안
  - Associative mapping(TLB)
  - PMT를 위한 전용 기억장치(공간) 사용
    - Dedicated register or cache memory
  - Hierarchical paging
  - Hashed page table
  - Inverted page table



#### Associative Mapping

- TLB(Translation Look-aside Buffer)에 PMT 적재
  - Associative high-speed memory
- PMT를 병렬 탐색
- Low overhead, high speed
- Expensive hardware
  - 큰 PMT를 다루기가 어려움



#### Hybrid Direct / Associative Mapping

- 두 기법을 혼합하여 사용
  - HW 비용은 줄이고, Associative mapping의 장점 활용
- 작은 크기의 TLB 사용
  - PMT : 메모리(커널 공간)에 저장
  - TLB : PMT 중 일부 entry들을 적재
    - 최근에 사용된 page들에 대한 entry 저장
  - Locality(지역성) 활용
    - 프로그램의 수행과정에서 한번 접근한 영역을 다시 접근(temporal locality) 또는 인접 영역을 다시 접근(spatial locality)할 가능성이 높음