# 104 DDL - CREATE TABLE

## DDL(Data Define Language, 데이터 정의어)

- DB 구조, 데이터 형식, 접근 방식 등 DB를 구축하거나 수정할 목적으로 사용하는 언어이다
- DDL은 번역한 결과가 데이터 사전(Data Dictionary)이라는 특별한 파일에 여러 개의 테이블로서 저장된다
- DDL에는 CREATE SCHEMA, CREATE DOMAIN, CREATE TABLE, CREATE VIEW, CREATE INDEX, ALTER TABLE, DROP 등이 있다



## CREATE TABLE

- 테이블을 정의하는 명령문이다

- 표기 형식

  - ```SQL
    CREATE TABLE 테이블명
    	(속성명 데이터_타입 [DEFAULT 기본값] [NOT NULL], ...
        [, PRIMARY KEY(기본키_속성명, ...)]
        [, UNIQUE(대체키_속성명, ...)]
        [, FOREIGN KEY(외래키_속성명, ...)]
        	[REFERENCES 참조테이블(기본키_속성명, ...)]
        	[ON DELETE 옵션]
        	[ON UPDATE 옵션]
        [, CONSTRAINT 제약조건명] [CHECK (조건식)]);
    ```

  - PRIMARY KEY : 기본키로 사용할 속성 또는 속성의 집합을 지정함

  - UNIQUE : 대체키로 사용할 속성 또는 속성의 집합을 지정하는 것으로 UNIQUE로 지정한 속성은 중복된 값을 가질 수 없음

  - FOREIGN KEY ~ REFERENCES ~

    - ON DELETE 옵션 : 참조 테이블의 튜플이 삭제되었을 때 기본 테이블에 취해야 할 사항을 지정함. 옵션에는 NO ACTION, CASCADE, SET NULL, SET DEFAULT가 있음
    - ON UPDATE 옵션 : 참조 테이블의 참조 속성 값이 변경되었을 때 기본 테이블에 취해야 할 사항을 지정함. 옵션에는 NO ACTION, CASCADE, SET NULL, SET DEFAULT가 있음

  - CONSTRAINT : 제약 조건의 이름을 지정함. 이름을 지정할 필요가 없으면 CHECK절만 사용하여 속성 값에 대한 제약 조건을 명시함

  - CHECK : 속성 값에 대한 제약 조건을 정의함



### 다른 테이블을 이용한 테이블 정의

- 기존 테이블의 정보를 이용해 새로운 테이블을 정의할 수 있다

- 표기 형식

  - ```SQL
    CREATE TABLE 신규테이블명 AS SELECT 속성명[, 속성명, ...] 
    	FROM 기존테이블명;
    ```