# 081 배치 프로그램(Batch Program)

- 사용자와의 상호 작용 없이 여러 작업들을 미리 정해진 일련의 순서에 따라 일괄적으로 처리하는 것을 의미한다
- 배치 프로그램이 자동으로 수행되는 주기에 따라 정기 배치, 이벤트성 배치, On-Demand 배치로 구분된다
- 배치 프로그램의 필수 요소 : 대용량 데이터, 자동화, 견고성, 안정성/신뢰성, 성능
- 배치 스케줄러(Batch Scheduler) : 일괄 처리(Batch Processing) 작업이 설정된 주기에 맞춰 자동으로 수행되도록 지원해주는 도구
- 주요 배치 스케줄러
  - 스프링 배치(Spring Batch)
    - Spring source 사와 Accenture 사가 2007년 공동 개발한 오픈소스 프레임워크이다
    - 로그 관리, 추적, 트랜잭션 관리, 작업 처리 통계, 작업 재시작 등의 다양한 기능을 제공한다
    - 주요 구성 요소 : Job, Job Launcher, Step, Job Repository
  - Quartz
    - 스프링 프레임워크로 개발되는 응용 프로그램들의 일괄 처리를 위한 다양한 기능을 제공하는 오픈 소스 라이브러리이다
    - 주요 구성 요소 : Scheduler, Job, JobDetail, Trigger
  - Cron
    - 리눅스의 스케줄러 도구로 crontab 명령어를 통해 작업을 예약할 수 있다