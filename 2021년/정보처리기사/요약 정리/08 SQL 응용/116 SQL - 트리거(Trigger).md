# 116 SQL - 트리거(Trigger)

- 데이터베이스 시스템에서 데이터의 삽입(Insert), 갱신(Update), 삭제(Delete) 등의 이벤트(Event)가 발생할 때마다 관련 작업이 자동으로 수행되는 절차형 SQL이다
- 트리거는 데이터베이스에 저장되며, 데이터 변경 및 무결성 유지, 로그 메시지 출력 등의 목적으로 사용된다



## 트리거 구성도

```SQL
DECLARE (필수)
EVENT (필수)
BEGIN (필수)
	CONTROL
	SQL
	EXCEPTION
END (필수)
```



## 트리거의 생성

```SQL
CREATE [OR REPLACE] TRIGGER 트리거명 [동작시기 옵션] [동작 옵션] ON 테이블명
REFERENCING [NEW | OLD] AS 테이블명
FOR EACH ROW
[WHEN 조건식]
BEGIN
	트리거 BODY;
END;
```



## 트리거의 제거

```SQL
DROP TRIGGER 트리거명;
```

