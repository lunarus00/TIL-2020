# 108 DCL - GRANT / REVOKE

## DCL(Data Control Language, 데이터 제어어)

- 데이터의 보안, 무결성, 회복, 병행 제어 등을 정의하는 데 사용하는 언어이다
- DCL은 데이터베이스 관리자(DBA)가 데이터 관리를 목적으로 사용한다
- DCL에는 GRANT, REVOKE, COMMIT, ROLLBACK, SAVEPOINT 등이 있다



## GRANT / REVOKE

- 데이터베이스 관리자가 데이터베이스 사용자에게 권한을 부여하거나 취소하기 위한 명령어이다

- GRANT : 권한 부여를 위한 명령어

- REVOKE : 권한 취소를 위한 명령어

- 사용자 등급 지정  및 해제

  - ```SQL
    GRANT 사용자등급 TO 사용자_ID_리스트 [IDENTIFIED BY 암호];
    ```

  - ```SQL
    REVOKE 사용자등급 FROM 사용자_ID_리스트;
    ```

- 테이블 및 속성에 대한 권한 부여 및 취소

  - ```SQL
    GRANT 권한_리스트 ON 개체 TO 사용자 [WITH GRANT OPTION];
    ```

  - ```SQL
    REVOKE [GRANT OPTION FOR] 권한_리스트 ON 개체 FROM 사용자
    	[CASCADE];
    ```

  - 권한 종류 : ALL, SELECT, INSERT, DELETE, UPDATE, ALTER 등

  - WITH GRANT OPTION : 부여받은 권한을 다른 사용자에게 다시 부여할 수 있는 권한을 부여함

  - GRANT OPTION FOR : 다른 사용자에게 권한을 부여할 수 있는 권한을 취소함

  - CASCADE : 권한 취소 시 권한을 부여받았던 사용자가 다른 사용자에게 부여한 권한도 연쇄적으로 취소함