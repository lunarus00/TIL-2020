# 115 프로시저(Procedure)

- 절차형 SQL을 활용하여 특정 기능을 수행하는 일종의 트랜잭션 언어로, 호출을 통해 실행되어 미리 저장해 놓은 SQL 작업을 수행한다
- 프로시저는 데이터베이스에 저장되어 수행되기 때문에 스토어드(Stored) 프로시저라고도 불린다
- 프로시저는 시스템의 일일 마감 작업, 일괄(Batch) 작업 등에 주로 사용된다



## 프로시저 구성도

```sql
DECLARE (필수)
BEGIN (필수)
	CONTROL
	SQL
	EXCEPTION
	TRANSACTION
END (필수)
```



## 프로시저 생성

```SQL
CREATE [OR REPLACE] PROCEDURE 프로시저명(파라미터)
[지역변수 선언]
BEGIN
	프로시저 BODY;
END;
```



## 프로시저 실행

```SQL
EXECUTE 프로시저명;
EXEC 프로시저명;
CALL 프로시저명;
```



## 프로시저 제거

```SQL
DROP PROCEDURE 프로시저명;
```

