"""
인자로 전달된 숫자를 이용해 카운트다운 하는 함수 countdown을 정의
countdown(0), countdown(10)을 순서대로 실행

"""

def countdown(number):
    if number == 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    for i in range(number):
        print(number - i)

countdown(0)
countdown(10)