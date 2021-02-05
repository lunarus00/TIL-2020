# 11 - 05 File System Implementation

## Allocation methods

- File 저장을 위한 디스크 공간 할당 방법

### Continuous allocation

- 한 File을 디스크의 연속된 block에 저장
- 장점
  - 효율적인 file 접근(순차, 직접 접근)
- 문제점
  - 새로운 file을 위한 공간 확보가 어려움
  - External fragmentation
  - File 공간 크기 결정이 어려움
    - 파일이 커녀야 하는 경우 고려해야 함



### Discontinuous allocation

- Linked allocation
  - File이 저장된 block들을 linked list로 연결
    - 비연속 할당 가능
  - Directory는 각 file에 대한 첫 번째 block에 대한 포인터를 가짐
  - Simple, No external fragmentation
  - 단점
    - 직접 접근에 비효율적
    - 포인터 저장을 위한 공간 필요
    - 신뢰성 문제
      - 사용자가 포인터를 실수로 건드리는 문제 등
  - File Allocation Table(FAT)
    - 각 block의 시작 부분에 다음 블록의 번호를 기록하는 방법
  - MS-DOS, Windows 등에 사용됨
- Indexed allocation
  - File이 저장된 block의 정보(pointer)를 Index block에 모아둠
  - 직접 접근에 효율적
    - 순차 접근에는 비효율적
  - File당 Index block을 유지
    - Space overhead
    - Index block 크기에 따라 파일의 최대 크기가 제한됨
  - Unix 등에 사용됨



## Free space management

- 디스크의 빈 공간 관리

### Bit vector

- 시스템 내 모든 block들에 대한 사용 여부를 1 bit flag로 표시
- Simple and efficient
- Bit vector 전체를 메모리에 보관해야 함
  - 대형 시스템에 부적합



### Linked List

- 빈 block을 linked list로 연결
- 비효율적



### Grouping

- n개의 빈 block을 그룹으로 묶고, 그룹 단위로 linked list로 연결
- 연속된 빈 block을 쉽게 찾을 수 있음



### Counting

- 연속된 빈 block들 중 첫 번째 block의 주소와 연속된 block의 수를 table로 유지
- Continuous allocation 시스템에 유리한 기법

