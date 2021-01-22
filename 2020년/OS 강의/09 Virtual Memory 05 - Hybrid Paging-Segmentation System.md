# 09 Virtual Memory 05 - Hybrid Paging-Segmentation System

## Hybrid Paging / Segmentation

- Paging과 Segmentation의 장점 결합
- 프로그램 분할
  - 논리 단위의 segment로 분할
  - 각 segment를 고정된 크기의 page들로 분할
- Page 단위로 메모리에 적재



### Address mapping

- Virtual address : v = (s, p, d)
  - s : segment number
  - p : page number
  - d : offset in a page
- SMT와 PMT 모두 사용
  - 각 프로세스마다 하나의 SMT
  - 각 segment마다 하나의 PMT
- Address mapping
  - Direct, associated 등
- 메모리 관리
  - FPM과 유사



### Summary

- 논리적 분할(segment)와 고정 크기 분할(page)을 결합
  - Page sharing / protection이 쉬움
  - 메모리 할당 / 관리 overhead가 작음
  - No external fragmentation
- 전체 테이블의 수 증가
  - 메모리 소모가 큼
  - Address mapping 과정이 복잡
- Direct mapping의 경우, 메모리 접근이 3배
  - 성능이 저하될 수 있음