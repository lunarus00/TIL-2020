# 113 DML - JOIN

## JOIN의 개념

- 2개의 테이블에 대해 연관된 튜플들을 결합하여 하나의 새로운 릴레이션을 반환한다
- JOIN은 크게 INNER JOIN과 OUTER JOIN으로 구분된다
- JOIN은 일반적으로 FROM절에 기술하지만, 릴레이션이 사용되는 어느 곳에서나 사용할 수 있다



## INNER JOIN

- 가장 일반적인 JOIN의 형태로, 관계가 설정된 두 테이블에서 조인된 필드가 일치하는 행만을 표시한다

- WHERE절을 이용한 표기 형식

  - ```SQL
    SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1, 테이블명2, ...
    WHERE 테이블명1.속성명 = 테이블명2.속성명;
    ```

- NATURAL JOIN을 이용한 표기 형식

  - ```SQL
    SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1 NATURAL JOIN 테이블명2;
    ```

- JOIN ~ USING 절을 이용한 표기 형식

  - ```SQL
    SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1 JOIN 테이블명2 USING(속성명);
    ```