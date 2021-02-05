# 12 - 03 RAID Architecture

## RAID Architecture

- Redundant Array of Inexpensive Disks(RAID)
- 여러 개의 물리 disk를 하나의 논리 disk로 사용
  - OS support, RAID controller
- Disk system의 성능 향상을 위해 사용
  - Performance(access speed)
  - Reliability



## RAID 0

- Disk striping
  - 논리적인 한 block을 일정한 크기로 나누어 각 disk에 나누어 저장
- 모든 disk에 입출력 부하 균등 분배
  - Parallel access
  - Performance 향상
- 한 Disk에서 장애 시 데이터 손실 발생
  - Low reliability



## RAID 1

- Disk mirroring
  - 동일한 데이터를 mirroring disk에 중복 저장
- 최소 2개의 disk로 구성
  - 입출력은 둘 중 어느 disk에서도 가능
- 한 disk에 장애가 생겨도 데이터 손실 없음
  - High reliability
- 가용 disk 용량 = 전체 disk 용량 / 2



## RAID 3

- RAID + parity disk
  - Byte 단위 분할 저장
  - 모든 disk에 입출력 부하 균등 분배
    - Parallel access, Performance 향상
- 한 disk에 장애 발생 시 parity 정보를 이용하여 복구
- Write 시 parity 계산 필요
  - Overhead
  - Write가 몰릴 시 병목현상 발생 가능



## RAID 4

- RAID 3과 유사, 단 Block 단위로 분산 저장
  - 독립된 access 방법
  - Disk간 균등 분배가 되지 않을 수 있음
  - 한 disk에 장애 발생 시 parity 정보를 이용하여 복구
  - Write 시 parity 계산 필요
    - Overhead / Write가 몰릴 시 병목현상 발생 가능
- 병목현상으로 성능 저하 가능
  - 한 disk에 입출력이 몰릴 때



## RAID 5

- RAID 4와 유사
  - 독립된 access 방법
- Parity 정보를 각 disk들에 분산 저장
  - Parity disk의 병목현상 문제 해소
- 현재 가장 널리 사용되는 RAID level 중 하나
  - High performance and reliability