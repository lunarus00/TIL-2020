# 09 Virtual Memory 04 - Segmentation System

## Segmentation System

- 프로그램(또는 process)을 논리적 block으로 분할(segment)
  - Block의 크기가 서로 다를 수 있음
  - 예) stack, heap, main procedure, shared lib, 등
- 특징
  - 메모리를 미리 분할하지 않음
    - VPM과 유사
  - Segment sharing / protection이 용이함
  - Address mapping 및 메모리 관리의 overhead가 큼
  - No internal fragmentation
    - External fragmmentation 발생 가능



### Address mapping

- Virtual address : v = (s, d)
  - s : segment number
  - d : displacement in a segment
- Segment Map Table (SMT)
- Address mapping mechanism
  - Paging system과 유사

1. 프로세스의 SMT가 저장되어 있는 주소 b에 접근
2. SMT에서 segment의 s의 entry 찾음
   - s의 entry 위치 = b + s * entrySize
3. 찾아진 Entry에 대해 다음 단계들을 순차적으로 실행
   1. 존재 비트가 0인 경우
      - missing segment fault
      - swap device로부터 해당 segment를 메모리로 적재
      - SMT를 갱신
   2. 변위(d)가 segment 길이보다 큰 경우 (d > ls), `segment overflow` exception 처리 모듈을 호출
   3. 허가되지 않은 연산일 경우 (protection bit field 검사), `segment protection` exception 처리 모듈을 호출
4. 실제 주소 r 계산 ( r = As + d)
5. r 로 메모리에 접근



### Memory management

- VPM과 유사
  - Segment 적재 시, 크기에 맞추어 분할 후 적재



### Segment sharing / protection

- 논리적으로 분할되어 있어 공유 및 보호가 용이함



### Segmentation System - Summary

- 프로그램을 논리 단위로 분할(segment) / 메모리를 동적으로 분할
  - 내부 단편화 문제 없음
  - Segment sharing / protection이 용이함
  - Paging system 대비 관리 overhead가 큼
- 필요한 segment만 메모리에 적재하여 사용
  - 메모리의 효율적 활용
- Segment mapping overhead
  - 메모리 공간 및 추가적인 메모리 접근이 필요
  - 전용 HW 활용으로 해결 가능