# 10 Virtual Memory Management 06 - Other considerations

## Page Size

- 시스템 특성에 따라 다름
  - No best answer
  - 점점 커지는 경향
- 일반적인 page size
  - 2^7(128) bytes ~ 2^22(4M) bytes
- Small page size
  - Large page table / # of PF
    - High overhead(kernel)
  - 내부 단편화 감소
  - I/O 시간 증가
  - Locality 향상
  - Page fault 증가
- Large page size
  - Small page table / # of PF
    - Low overhead(kernel)
  - 내부 단편화 증가
  - I/O 시간 감소
  - Locality 저하
  - Page fault 감소
- HW 발전 경향
  - CPU, Memory size up
  - 상대적인 Page fault 처리 비용 증가
  - 이로 인해 page size도 점점 커지는 경향이 있다



## Program Restructuring

- 가상 메모리 시스템의 특성에 맞도록 프로그램을 재구성
- 사용자가 가상 메모리 관리 기법(ex, paging system)에 대해 이해하고 있다면, `프로그램의 구조를 변경`하여 성능을 높일 수 있음



## TLB Reach

- TLB를 통해 접근할 수 있는 메모리의 양
  - (The number of entries) * (the page size)
- TLB의 hit ratio를 높이려면
  - TLB의 크기 증가
    - Expensive
  - Page 크기 증가 or 다양한 page size 지원
    - OS의 지원이 필요
      - 최근 OS의 발전 경향