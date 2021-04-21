# 105 DDL - CREATE VIEW

- 뷰(View)를 정의하는 명령문이다

- 표기 형식

  - ```SQL
    CREATE VIEW 뷰명[(속성명[, 속성명, ...])]
    AS SELECT문;
    ```

  - SELECT문을 서브 쿼리로 사용하여 SELECT문의 결과로서 뷰를 생성한다

  - 서브 쿼리인 SELECT문에는 UNION이나 OREDER BY절을 사용할 수 없다

  - 속성명을 기술하지 않으면 SELECT문의 속성명이 자동으로 사용된다