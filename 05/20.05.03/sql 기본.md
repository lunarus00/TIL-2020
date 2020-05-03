## sql 기본

- sql문은 대문자가 아니라 소문자로 작성해도 상관없음
- 단, 구분을 위해 대문자로 작성



#### 테이블 생성

- ```sql
  CREATE TABLE tablename (
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER,
      address TEXT
  );
  ```

  - AUTOINCREMENT : 자동으로 증가
  - name, age, address 등은 내용을 넣을 column에 따라 바뀌어짐.



#### 테이블 삭제

- ```sql
  DROP TABLE tablename;
  ```

  - tablename에 해당하는 테이블을 삭제함



#### 데이터 생성

- ```sql
  INSERT INTO tablename (column1, ~) VALUES (value1, ~);
  ```

  - column과 그에 들어갈 value를 하나씩 매칭시켜 데이터를 삽입함

- ```sql
  INSERT INTO tablename VALUES (id, name, age, address);
  ```

  - 모든 열에 데이터를 넣을 경우 column을 명시할 필요가 없음
  - 단, id 값도 함께 입력해 주어야 함



#### 데이터 읽기

- ```sql
  SELECT * FROM tablename WHERE condition;
  ```

  - `*` 부분은 모든 항목을 읽어들인다는 뜻
  - FROM으로 어느 테이블에서 가져올 것인지 지정
  - WHERE로 어떤 조건에 맞춰서 가져올 것인지 지정함

- ```sql
  SELECT column1, ~ FROM tablename WHERE condition;
  ```

  - 원하는 column을 지정해서 읽어들일 수 있음
  - 여러 column을 지정할 수도 있음



#### 데이터 삭제

- ```sql
  DELETE FROM tablename WHERE condition;
  ```

  - 특정한 테이블의 condition에 맞는 column을 삭제함



#### 데이터 수정

- ```sql
  UPDATE tablename SET column1=value1, ~ WHERE condition;
  ```

  - tablename 테이블의 WHERE 조건에 맞는 레코드를 SET 내용에 맞춰 수정



#### 데이터 조회

- 기본

  ```sql
  SELECT <column> FROM <table> 
  [WHERE <condition>] 
  [GROUP BY <column>] 
  [ORDER BY <column [ASC/DESC]>] 
  [LIMIT <integer>]
  [OFFSET <integer>];
  ```

  - WHERE : 조회할 조건 설정

  - GROUP : 특정 컬럼을 기준으로 그룹화

    - ```sql
      SELECT sex, COUNT(name) FROM classmates GROUP BY sex;
      ```

      - 성별에 따라 그룹화하고, name을 기준으로 count(김ㅇㅇ 이ㅇㅇ)
      - 이후 그룹에 따른 숫자를 제시함
      - 남자 30, 여자 35 등

  - ORDER : 정렬

    - ASC : 오름차순 - 미설정 시 기본 설정됨
    - DESC : 내림차순

  - LIMIT : 원하는 개수만큼

  - OFFSET : 앞에서부터 원하는 개수만큼 지나침

- COUNT(column)

- AVG(column)

- SUM(column)

- MAX(column)

- MIN(column)

- AND|OR

  - ```sql
    WHERE name='김' AND age>=18;
    ```

  - or문의 경우도 마찬가지로 사용함

- LIKE 

  - ```sql
    WHERE column LIKE 'pattern';
    ```

  - column에서 특정 pattern에 맞는 데이터를 조회

  - '010-%' 일 경우 010- 로 시작하는 데이터를 조회함

