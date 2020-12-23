## 107 DML-JOIN

#### JOIN의 개념

- JOIN은 2개의 테이블에 대해 연관된 튜플들을 결합하여, 하나의 새로운 일레이션을 반환한다
- JOIN은 크게 INNER JOIN과 OUTER JOIN으로 구분된다
- JOIN은 일반적으로 FROM절에 기술하지만, 릴레이션이 사용되는 어느 곳에서산 사용할 수 있다



#### INNER JOIN

- INNER JOIN은 일반적으로 EQUI JOIN과 NON-EQUI JOIN으로 구분된다

- 조건이 없는 INNER JOIN을 수행하면 CROSS JOIN과 동일한 결과를 얻을 수 있다

- EQUI JOIN

  - EQUI JOIN은 JOIN 대상 테이블에서 공통 속성을 기준으로 '='(equal) 비교에 의해 같은 값을 가지는 행을 연결하여 결과를 생성하는 JOIN 방법이다

  - EQUI JOIN에서 JOIN 조건이 '=' 일 때 동일한 속성이 두 번 나타나게 되는데, 이 중 중복된 속성을 제거하여 같은 속성을 한 번만 표기하는 방법을 NATURAL JOIN이라고 한다

  - EQUI JOIN에서 연결 고리가 되는 공통 속성을 JOIN 속성이라고 한다

  - WHERE 절을 이용한 EQUI JOIN의 표기 형식

    - ```SQL
      SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
      FROM 테이블명1, 테이블명2, ...
      WHERE 테이블명1.속성명 = 테이블명2.속성명;
      ```

  - NATURAL JOIN절을 이용한 EQUI JOIN의 표기 형식

    - ```SQL
      SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
      FROM 테이블명1 NATURAL JOIN 테이블명2;
      ```

  - JOIN ~ USING 절을 이용한 EQUI JOIN의 표기 형식

    - ```SQL
      SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
      FROM 테이블명1 JOIN 테이블명2 USING(속성명);
      ```

- NON-EQUI JOIN

  - NON-EQUI JOIN은 JOIN 조건에 '=' 조건이 아닌 나머지 비교 연산자, 즉 `>, <, <>, >=, <=` 연산자를 사용하는 JOIN 방법이다

  - 표기 형식

    - ```SQL
      SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
      FROM 테이블명1, 테이블명2, ...
      WHERE (NON-EQUI JOIN 조건);
      ```



#### OUTER JOIN

- OUTER JOIN은 릴레이션에서 JOIN 조건에 만족하지 않는 튜플도 결과로 출력하기 위한 JOIN 방법으로, LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN이 있다

- LEFT OUTER JOIN : INNER JOIN의 결과를 구한 후, 우측 항 릴레이션의 어떤 튜플과도 맞지 않는 좌측 항의 릴레이션에 있는 튜플들에 NULL 값을 붙여서 INNER JOIN의 결과에 추가한다

  - ```SQL
    SELEFT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1 LEFT OUTER JOIN 테이블명2
    ON 테이블명1.속성명 = 테이블명2. 속성명;
    ```

  - ```SQL
    SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1, 테이블명2
    WHERE 테이블명1.속성명 = 테이블명2.속성명(+);
    ```

- RIGHT OUTER JOIN : INNER JOIN의 결과를 구한 후, 좌측 항 릴레이션의 어떤 튜플과도 맞지 않는 우측 항의 릴레이션에 있는 튜플들에 NULL 값을 붙여서 INNER JOIN의 결과에 추가한다

  - ```SQL
    SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1 RIGHT OUTER JOIN 테이블명2
    ON 테이블명1.속성명 = 테이블명2.속성명;
    ```

  - ```SQL
    SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1, 테이블명2
    WHERE 테이블명1.속성명(+) = 테이블명2.속성명;
    ```

- FULL OUTER JOIN

  - LEFT OUTER JOIN과 RIGHT OUTER JOIN을 합쳐 놓은 것이다

  - INNER JOIN의 결과를 구한 후, 좌측 항의 릴레이션의 튜플들에 대해 우측 항의 릴레이션의 어떤 튜플과도 맞지 않는 튜플들에 NULL 값을 붙여서 INNER JOIN의 결과에 추가한다. 그리고 유사하게 우측 항의 릴레이션의 튜플들에 대해 좌측 항의 릴레이션의 어떤 튜플과도 맞지 않는 튜플들에 NULL 값을 붙여서 INNER JOIN의 결과에 추가한다

  - ```SQL
    SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
    FROM 테이블명1 FULL OUTERJ JOIN 테이블명2
    ON 테이블명1.속성명 = 테이블명2.속성명;
    ```



#### SELF JOIN

- SELF JOIN은 같은 테이블에서 2개의 속성을 연결하여 EQUI JOIN을 하는 JOIN 방법이다

- 표기 형식

  - ```SQL
    SELECT [별칭1.]속성명, [별칭1.]속성명, ...
    FROM 테이블명1 [AS] 별칭1 JOIN 테이블명1 [AS] 별칭2
    ON 별칭1.속성명 = 별칭2.속성명;
    ```

  - ```SQL
    SELECT [별칭1.]속성명, [별칭1.]속성명, ...
    FROM 테이블명1 [AS] 별칭1, 테이블명1 [AS] 별칭2
    WHERE 별칭1.속성명 = 별칭2.속성명;
    ```

- SELF JOIN의 이해

  - SELF JOIN은 1개의 테이블을 2개의 이름으로 사용하므로 종종 결과가 혼동된다. 이럴 때는 같은 테이블을 2개 그려서 생각하면 쉽게 결과를 알아낼 수 있다.