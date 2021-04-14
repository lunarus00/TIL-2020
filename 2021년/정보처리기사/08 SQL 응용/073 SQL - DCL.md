# 073 SQL - DCL

## 1 DCL(Data Control Language, 데이터 제어어)의 개념

- DCL(데이터 제어어)는 데이터의 보안, 무결성, 회복, 병행 제어 등을 정의하는 데 사용하는 언어이다
- DCL은 데이터베이스 관리자(DBA)가 데이터 관리를 목적으로 사용한다
- DCL에는 GRANT, REVOKE, COMMIT, ROLLBACK, SAVEPOINT 등이 있다



## 2 GRANT / REVOKE

- 데이터베이스 관리자가 데이터베이스 사용자에게 권한을 부여하거나 취소하기 위한 명령어이다

- GRANT : 권한 부여를 위한 명령어

- REVOKE : 권한 취소를 위한 명령어

- 사용자등급 지정 및 해제

  - ```SQL
    GRANT 사용자등급 TO 사용자_ID_리스트 [IDENTIFIED BY 암호];
    REVOKE 사용자등ㅇ급 FROM 사용자_ID_리스트;
    ```

  - 사용자등급

    - DBA : 데이터베이스 관리자
    - RESOURCE : 데이터베이스 및 테이블 생성 가능자
    - CONNECT : 단순 사용자

- 테이블 및 속성에 대한 권한 부여 및 취소

  - ```sql
    GRANT 권한_리스트 ON 개체 TO 사용자 [WITH GRANT OPTION];
    REVOKE [GRANT OPTION FOR] 권한_리스트 ON 개체 FROM 사용자 [CASCADE];
    ```

  - 권한 종류 : ALL, SELECT, INSERT, DELETE, UPDATE, ALTER 등

  - WITH GRANT OPTION : 부여받은 권한을 다른 사용자에게 다시 부여할 수 있는 권한을 부여함

  - GRANT OPTIION FOR : 다른 사용자에게 권한을 부여할 수 있는 권한을 취소함

  - CASCADE : 권한 취소 시 권한을 부여받았던 사용자가 다른 사용자에게 부여한 권한도 연쇄적으로 취소함



## 3 COMMIT

- 트랜잭션이 성공적으로 끝나면 데이터베이스가 새로운 일관성(Consistency) 상태를 가지기 위해 변경된 모든 내용을 데이터베이스에 반영하여야 하는데, 이때 사용하는 명령이 COMMIT이다
- COMMIT 명령을 실행하지 않아도 DML문이 성공적으로 완료되면 자동으로 COMMIT되고, DML이 실패하면 자동으로 ROLLBACK이 되도록 Auto Commit 기능을 설정할 수 있다



## 4 ROLLBACK

- ROLLABCK은 아직 COMMIT되지 않은 변경된 모든 내용들을 취소하고 데이터베이스를 이전 상태로 되돌리는 명령어이다
- 트랜잭션 전체가 성공적으로 끝나지 못하면 일부 변경된 내용만 데이터베이스에 반영되는 비일관성(Inconsistency)인 상태를 가질 수 있기 때문에 일부분만 완료된 트랜잭션은 롤백(Rollback)되어야 한다



## 5 SAVEPOINT

- SAVEPOINT는 트랜잭션 내에 ROLLBACK 할 위치인 저장점을 지정하는 명령어이다
- 저장점을 지정할 때는 이름을 부여하며, ROLLBACK 시 지정된 저장점까지의 트랜잭션 처리 내용이 취소된다

