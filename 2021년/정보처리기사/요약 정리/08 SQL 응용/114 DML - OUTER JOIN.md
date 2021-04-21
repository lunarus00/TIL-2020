# 114 DML - OUTER JOIN

- 릴레이션에서 JOIN 조건에 만족하지 않는 튜플도 결과로 출력하기 위한 JOIN 방법으로, LEFT OUTER JOIN, RIGHT OUTER JOIN 등이 있다

- LEFT OUTER JOIN : INNER JOIN의 결과를 구한 후, 우측 항 릴레이션의 어떤 튜플과도 맞지 않는 좌측 항의 릴레이션에 있는 튜플들에 NULL 값을 붙여서 INNER JOIN의 결과에 추가함

  - 표기 형식

    - ```SQL
      SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
      FROM 테이블명1 LEFT OUTER JOIN 테이블명2
      ON 테이블명1.속성명 = 테이블명2.속성명;
      ```

- RIGHT OUTER JOIN : INNER JOIN의 결과를 구한 후, 좌측 항 릴레이션의 어떤 튜플과도 맞지 않는 우측 항의 릴레이션에 있는 튜플들에 NULL 값을 붙여서 INNER JOIN의 결과에 추가함

  - 표기 형식

    - ```SQL
      SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
      FROM 테이블명1 RIGHT OUTER JOIN 테이블명2
      ON 테이블명1.속성명 = 테이블명2.속성명;
      ```