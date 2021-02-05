# 12 - 01 I/O System

## I/O Mechanisms

- How to send data between processor and I/O device

### Processor controlled memory access

#### Polling (Programmed I/O)

- Processor가 주기적으로 I/O 장치의 상태 확인
  - 모든 I/O 장ㅇ치를 순환하며 확인
  - 전송 준비 및 전송 상태 등
- 장점
  - Simple
  - I/O 장치가 빠르고, 데이터 전송이 잦은 경우 효율적
- 단점
  - Processor의 부담이 큼
    - Pooling overhead (I/O device가 느린 경우)

#### Interrupt

- I/O 장치가 작업을 완료한 후, 자신의 상태를 Processor에게 전달
  - Interrupt 발생 시, Processor는 데이터 전송 수행
- 장점
  - Pooling 대비 low overhead
  - 불규칙적인 요청 처리에 적합
- 단점
  - Interrupt handling overhead



### Direct Memory Access(DMA)

- Processor controlled memory access 방법
  - Processor가 모든 데이터 전송을 처리해야 함
    - High overhead for the processor
- Direct Memory Access
  - I/O 장치와 Memory 사이의 데이터 전송을 Processor 개입 없이 수행
- Processor는 데이터 전송의 시작/종료에만 관여
  1. 프로세서가 전송 방향, 전송 바이트 수, 데이터 블록의 메모리 주소 등을 DMA 제어기에 보낸다
  2. DMA 제어기는 디스크 제어기에 데이터를메인 메모리로 전송하라고 요청한다
  3. 디스크 제어기가 메인 메모리에 데이터를 전송한다
  4. 데이터 전송을 완료하면 디스크 제어기는 DMA 제어기에 완료 메시지를 전달한다
  5. DMA 제어기가 프로세서에 인터럽트 신호를 보낸다



## I/O Services of OS

- OS Supports for better I/O performance



#### I/O Scheduling

- 입출력 요청에 대한 처리 순서 결정
  - 시스템의 전반적 성능 향상
  - Process의 요구에 대한 공평한 처리

- E.g, Disk I/O scheduling



#### Error handling

- 입출력 중 발생하는 오류 처리
- E.g, disk access fail, network communication error 등



#### I/O device information managements

- Buffering
  - I/O 장치와 Program 사이에 전송되는 데이터를 Buffer에 임시 저장
  - 전송 속도(or 처리 단위) 차이 문제 해결



#### Caching

- 자주 사용하는 데이터를 미리 복사해 둠
- Cache hit 시 I/O를 생략할 수 있음



### Spooling

- 한 I/O 장치에 여러 Program이 요청을 보낼 시, 출력이 섞이지 않도록 하는 기법
  - 각 Program에 대응하는 disk file에 기록(spooling)
  - Spooling이 완료되면 spool을 한번에 하나씩 I/O 장치로 전송