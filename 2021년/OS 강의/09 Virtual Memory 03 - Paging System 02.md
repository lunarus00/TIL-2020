# 09 Virtual Memory 03 - Paging System 02

## Memory Management

- Page와 같은 크기로 미리 분할하여 관리 / 사용
  - Page frame
  - FPM 기법과 유사
- Frame table
  - Page frame당 하나의 entry
  - 구성
    - Allocated / available field
    - PID field
    - Link field : For free list (사용가능한 fp들을 연결)
    - AV : Free list header(free list의 시작점)



### Page Sharing

- 여러 프로세스가 특정 page를 공유 가능
  - Non-continuous allocation
- 공유 가능 page
  - Procedure pages
    - Pure code(reenter code)
  - Data page
    - Read-only data
    - Read-write data
      - 병행성(concurrency) 제어 기법 관리하에서만 가능
- Procedure Page Sharing(Solution)
  - 프로세스들이 shared page에 대한 정보를 PMT의 같은 entry에 저장하도록 함



### Paging System - Summary

- 프로그램을 고정된 크기의 block으로 분할(page) / 메모리를 block size로 미리 분할(page frame)
  - 외부 단편화 문제 없음
  - 메모리 통합 / 압축 불필요
  - 프로그램의 논리적 구조 고려하지 않음
    - Page sharing / protection이 복잡
- 필요한 page만 page frame에 적재하여 사용
  - 메모리의 효율적 활용
- Page mapping overhead
  - 메모리 공간 및 추가적인 메모리 접근이 필요
  - 전용 HW 활용으로 해결 가능
    - 하드웨어 비용 증가