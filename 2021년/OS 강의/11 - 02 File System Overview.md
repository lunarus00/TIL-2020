# 11 - 02 File System Overview

## File System

- 사용자들이 사용하는 파일들을 관리하는 운영체제의 한 부분
- File System의 구성
  - Files
    - 연관된 정보의 집합
  - Directory structure
    - 시스템 내 파일들의 정보를 구성 및 제공
  - Partitions
    - Directory들의 집합을 논리적/물리적으로 구분



### File Concept

- 보조 기억 장치에 저장된 연관된 정보들의 집합
  - 보조기억장치 할당의 최소 단위
  - Sequence of bytes(물리적 정의)
- 내용에 따른 분류
  - Program file
    - Source program, object program, executable files
  - Data file
- 형태에 따른 분류
  - Text (ascii) file
  - Binary file
- File attributes(속성)
  - Name
  - Identifier
  - Type
  - Location
  - Size
  - Protection
    - access control information
  - User identification(owner)
  - Time, date
    - creation, late reference, last modification
- File operations
  - Create
  - Write
  - Read
  - Reposition
  - Delete
  - Etc.
- OS는 file operation들에 대한 system call을 제공해야 함



### File Access Methods

- Sequential access(순차 접근)
  - File을 record(or bytes)단위로 순서대로 접근
    - E.g., fgetc()
- Directed access(직접 접근)
  - 원하는 Block에 직접 접근
    - E.g., lseek(), seek()
- Indexed access
  - Index를 참조하여, 원하는 block을 찾은 후 데이터에 접근



## File System Organization

- Partitions(minidisks, volumes)
  - Virtual disk
- Directory
  - File들을 분류, 보관하기 위한 개념
  - Operations on directory
    - Search for a file
    - Create a file
    - Delete a file
    - List a directory
    - Rename a file
    - Traverse the file system



## Mounting

- 현재 FS에 다른 FS를 붙이는 것