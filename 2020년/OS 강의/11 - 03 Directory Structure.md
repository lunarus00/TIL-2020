# 11 - 03 Directory Structure

## Directory Structure

### Logical directory structure

#### Flat (single-level) directory Structure

- FS내에 하나의 directory만 존재
  - Single-level directory structure
- Issues
  - File naming
  - File protection
  - File management
  - 다중 사용자 환경에서 문제가 더욱 커짐



#### 2-Level Directory Structure

- 사용자마다 하나의 directory 배정
- 구조
  - MFD(Master File Directory)
  - UFD(User File Directory)
- Problems
  - Sub-directory 생성 불가능
    - File naming issue
  - 사용자간 파일 공유 불가

#### Hierarchical Directory Structure

- Tree 형태의 계층적 directory 사용 가능
- 사용자가 하부 directory 생성/관리 가능
  - System call이 제공되어야 함
  - Terminologies
    - Home directory, Current directory
    - Absolute pathname, Relative pathname
- 대부분의 OS가 사용



#### Acyclic Graph Directory Structure

- Hierarchical directory structure 확장
- Directory 안에 shared directory, shared file 을 담을 수 있음
- Link의 개념 사용
  - E.g., Unix system의 symbolic link
- cycle 비허용



#### General Graph Directory Structure

- Acyclic Graph Directory Structure의 일반화
  - Cycle을 허용
- Problems
  - File 탐색 시, Infinite loop를 고려해야 함