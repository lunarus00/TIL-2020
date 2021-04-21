# 106 DDL - ALTER TABLE

- 테이블에 대한 정의를 변경하는 명령문이다

- 표기 형식

  - ```SQL
    ALTER TABLE 테이블명 ADD 속성명 데이터_타입 [DEFAULT '기본값'];
    ALTER TABLE 테이블명 ALTER | MODIFY 속셩명 [SET DEFAULT '기본값'];
    ALTER TABLE 테이블명 DROP COLUMN 속성명 [CASCADE];
    ```

  - ADD : 새로운 속성(열)을 추가할 때 사용

  - ALTER | MODIFY : 특정 속성의 정의를 변경할 때 사용

  - DROP COLUMN : 특정 속성을 삭제할 때 사용