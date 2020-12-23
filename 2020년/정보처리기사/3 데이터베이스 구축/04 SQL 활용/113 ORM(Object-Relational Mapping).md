## 113 ORM(Object-Relational Mapping)

#### ORM(Object-Relational Mapping)의 개요

- ORM은 객체지향 프로그래밍의 객체(Object)와 관계형 데이터베이스(Relational Database)의 데이터를 연결(Mapping)하는 기술을 의미한다
- ORM은 객체지향 프로그래밍에서 사용할 수 있는 가상의 객체지향 데이터베이스를 만들어 프로그래밍 코드와 데이터를 연결한다
- ORM으로 생성된 가상의 객체지향 데이터베이스는 프로그래밍 코드 또는 데이터베이스와 독립적이므로 재사용 및 유지보수가 용이하다
- ORM은 SQL 코드를 직접 입력하지 않고 선언문이나 할당 같은 부수적인 코드가 생략되기 때문에 직관적이고 간단하게 데이터를 조작할 수 있다



#### ORM 프레임워크

- ORM 프레임워크는 ORM을 구현하기 위한 구조와 구현을 위해 필요한 여러 기능들을 제공하는 소프트웨어를 의미한다
- ORM 프레임워크의 종류
  - JAVA : JPA, Hibernate, EclipseLink, DataNucleus, Ebean 등
  - C++ : ODB, QxOrm 등
  - Python : Django, SQLAIchemy, Storm 등
  - iOS : DatabaseObjects, Core Data 등
  - .NET : NHibernate, DatabaseObjects, Dapper 등
  - PHP : Doctrine, Propel, RedBean 등



#### ORM의 한계

- ORM은 프레임워크가 자동으로 SQL을 작성하기 때문에 의도대로 SQL이 작성되었는지 확인할 필요가 있다
- 객체지향적인 사용을 고려하고 설계된 데이터베이스가 아닌 경우 프로젝트가 크고 복잡해질수록 ORM 기술을 적용하기 어려워진다
- 기존의 기업들은 ORM을 고려하지 않은 데이터베이스를 사용하고 있기 때문에 ORM에 적합하게 변환하려면 많은 시간과 노력이 필요하다