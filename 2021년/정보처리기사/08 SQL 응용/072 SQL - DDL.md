# 072 SQL - DDL

## 1 DDL(Data Define Language, 데이터 정의어)의 개념

- DDL(데이터 정의어)는 DB 구조, 데이터 형식, 접근 방식 등 DB를 구축하거나 수정할 목적으로 사용하는 언어이다
- DDL은 번역한 결과가 데이터 사전(Data Dictionary)이라는 특별한 파일에 여러 개의 테이블로서 저장된다
- DDL에는 CREATE SCHEMA, CREATE DOMAIN, CREATE TABLE, CREATE VIEW, CREATE INDEX, ALTER TABLE, DROP 등이 있다



## 2 CREATE SCHEMA

- CREATE SCHEMA는 스키마를 정의하는 명령문이다

  - 스키마(Schema)
    - 데이터베이스의 구조와 제약 조건에 관한 전반적인 명세를 기술한 것으로 데이터 개체, 속성, 관계 및 데이터 조작 시 데이터 값들이 갖는 제약 조건 등에 관해 전반적으로 정의한다

- 스키마의 식별을 위해 스키마 이름과 소유권자나 허가권자를 정의한다

- 표기형식

  - ```SQL
    CREATE SCHEMA 스키마명 AUTHORIZATION 사용자_id;
    ```





## 3 CREATE DOMAIN

- CREATE DOMAIN은 도메인을 정의하는 명령문이다

  - 도메인
    - 하나의 속성이 취할 수 있는 동일한 유형의 원자값들의 집합을 의미한다
    - 특정 속성에서 사용할 데이터의 범위를 사용자가 정의하는 사용자 정의 데이터 타입

- 임의의 속성에서 취할 수 있는 값의 범위가 SQL에서 지원하는 전체 데이터 타입의 값이 아니고 일부분일 때, 사용자는 그 값의 범위를 도메인으로 정의할 수 있다

- 정의돈 도메인명은 일반적인 데이터 타입처럼 사용한다

- 표기 형식

  - ```SQL
    CREATE DOMAIN 도메인명 [AS] 데이터_타입
    		[DEFAULT 기본값]
    		[CONSTRAINT 제약조건명 CHECK (범위값)];
    ```

  - 데이터 타입 : SQL에서 지원하는 데이터 타입

  - 기본값 : 데이터를 입력하지 않았을 때 자동으로 입력되는 값



## 4 CREATE TABLE

- CREATE TABLE은 테이블을 정의하는 명령문이다

  - 테이블
    - 테이블은 데이터베이스의 설계 단계에서는 주로 릴레이션이라 부르고, 조작이나 검색 시에는 테이블이라고 부른다. 대부분 구분 없이 사용한다

- 표기 형식

  - ```SQL
    CREATE TABLE 테이블명
    		(속성명 데이터_타입 [DEFAULT 기본값] [NOT NULL], ...
            [, PRIMARY KEY(기본키_속성명, ...)]
            [, UNIQUE(대체키_속성명, ...)]
            [, FOREIGN KEY(외래키_속성명, ...)
            	REFERENCES 참조테이블(기본키_속성명, ...)]
            	[ON DELETE 옵션]
             	[ON UPDATE 옵션]
            [, CONSTRAINT 제약조건명] [CHECK (조건식)]);
    ```

  - 기본 테이블에 포함도리 모든 속성에 대하여 속성명과 그 속성의 데이터 타입, 기본값, NOT NULL 여부를 지정한다

  - PRIMARY KEY : 기본키로 사용할 속성 또는 속성의 집합을 지정한다

  - UNIQUE : 대체키로 사용할 속성 또는 속성의 집합을 지정하는 것으로 UNIQUE로 지정한 속성은 중복된 값을 가질 수 없다

  - FOREIGN KEY ~ REFERENCES ~

    - 참조할 다른 테이블과 그 테이블을 참조할 때 사용할 외래키 속성을 지정한다
    - 외래키가 지정되면 참조 무결성의 CASCADE 법칙이 적용된다
    - ON DELETE 옵션
      - 참조 테이블의 튜플이 삭제되었을 때 기본 테이블에 취해야 할 사항을 지정한다. 옵션에는 NO ACTION, CASCADE, SET NULL, SET DEFAULT가 있다
    - ON UPDATE 옵션
      - 참조 테이블의 참조 속성 값이 변경되었을 때 기본 테이블에 취해야 할 사항을 지정한다. 옵션에는 NO ACTION, CASCADE, SET NULL, SET DEFAULT가 있다
    - NO ACTION : 참조 테이블에 변화가 있어도 기본 테이블에는 아무런 조치를 취하지 않는다
    - CASCADE : 참조 테이블의 튜플이 삭제되면 기본 테이블의 관련 튜플도 모두 삭제되고, 속성이 변경되면 관련 튜플의 속성 값도 모두 변경된다
    - SET NULL : 참조 테이블에 변화가 있으면 기본 테이블의 관련 튜플의 속성 값을 NULL로 변경한다
    - SET DEFAULT : 참조 테이블에 변화가 있으면 기본 테이블의 관련 튜플의 속성 값을 기본값으로 변경한다

  - CONSTRAINT : 제약 조건의 이름을 지정한다. 이름을 지정할 필요가 없으면 CHECK절만 사용하여 속성 값에 대한 제약 조건을 명시한다

  - CHECK : 속성 값에 대한 제약 조건을 정의한다



## 5 CREATE VIEW

- CREATE VIEW는 뷰(View)를 정의하는 명령문이다

  - 뷰는 물리적으로 구현되지 않는다.(테이블은 물리적으로 구현되어 데이터가 저장됨)
  - 뷰를 생성하면 뷰 정의가 시스템 내에 저장되어 있다가 SQL 내에서 뷰 이름을 사용하면 실행 시간에 뷰 정의가 대체되어 수행된다

- 표기 형식

  - ```SQL
    CREATE VIEW 뷰명[(속성명[, 속성명, ...])]
    AS SELECT문;
    ```

  - SELECT문을 서브 쿼리로 사용하여 SELECT문의 결과로서 뷰를 생성한다

  - 서브 쿼리인 SELECT문에는 UNION이나 ORDER BY절을 사용할 수 없다

  - 속성명을 기술하지 않으면 SELECT문의 속성명이 자동으로 사용된다



## 6 CREATE INDEX

- CREATE INDEX는 인덱스를 정의하는 명령문이다

  - 인덱스는 검색 시간을 단축시키기 위해 만든 보조적인 데이터 구조이다

- 표기 형식

  - ```SQL
    CREATE [UNIQUE] INDEX 인덱스명
    ON 테이블명(속성명 [ASC | DESC] [, 속성명 [ASC | DESC]])
    [CLUSTER];
    ```

  - UNIQUE

    - 사용된 경우 : 중복 값이 없는 속성으로 인덱스를 생성한다
    - 생략된 경우 : 중복 값을 허용하는 속성으로 인덱스를 생성한다

  - 정렬 여부 지정

    - ASC : 오름차순 정렬
    - DESC : 내림차순 정렬
    - 생략된 경우 : 오름차순으로 정렬됨

  - CLUSTER : 사용하면 인덱스가 클러스터드 인덱스로 설정됨

    - 인덱스 키의 순서에 따라 데이터가 정렬되어 저장되는 방식
    - 실제 데이터가 순서대로 저장되어 있어 인덱스를 검색하지 않아도 원하는 데이터를 빠르게 찾을 수 있다
    - 데이터 삽입, 삭제 발생 시 순서를 유지하기 위해 데이터를 재정렬함



## 7 ALTER TABLE

- ALTER TABLE은 테이블에 대한 정의를 변경하는 명령문이다

- 표기 형식

  - ```SQL
    ALTER TABLE 테이블명 ADD 속성명 데이터_타입 [DEFAULT '기본값'];
    ALTER TABLE 테이블명 ALTER 속성명 [SET DEFAULT '기본값'];
    ALTER TABLE 테이블명 DROP COLUMN 속성명 [CASCADE];
    ```

  - ADD : 새로운 속성(열)을 추가할 때 사용한다

  - ALTER : 특정 속성의 Default 값을 변경할 때 사용한다

  - DROP COLUMN : 특정 속성을 삭제할 때 사용한다



## 8 DROP

- DROP은 스키마, 도메인 기본 테이블, 뷰 테이블, 인덱스, 제약 조건 등을 제거하는 명령문이다

- 표기 형식

  - ```SQL
    DROP SCHEMA 스키마명 [CASCADE | RESTRICTED];
    DROP DOMAIN 도메인명 [CASCADE | RESTRICTED];
    DROP TABLE 테이블명 [CASCADE | RESTRICTED];
    DROP VIEW 뷰명 [CASCADE | RESTRICTED];
    DROP INDEX 인덱스명 [CASCADE | RESTRICTED];
    DROP CONSTRAINT 제약조건명;
    ```

  - DROP SCHEMA : 스키마를 제거한다

  - DROP DOMAIN : 도메인을 제거한다

  - DROP TABLE : 테이블을 제거한다

  - DROP VIEW : 뷰를 제거한다

  - DROP INDEX : 인덱스를 제거한다

  - DROP CONSTRAINT : 제약 조건을 제거한다

  - CASCADE : 제거할 요소를 참조하는 다른 모든 개체를 함께 제거한다. 즉 주 테이블의 데이터 제거 시 각 외래키와 관계를 맺고 있는 모든 데이터를 제거하는 참조 무결성 제약 조건을 설정하기 위해 사용된다

  - RESTRICTED : 다른 개체가 제거할 요소를 참조중일 때는 제거를 취소한다