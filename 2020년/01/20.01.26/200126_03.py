"""
가변형 인자를 정수로 받아 곱을 반환하는 함수 정의
1, 2, '4', 3과 같이 예외처리
'에러발생' 문구
"""

def count_num(*a):
    for i in range(len(a)):
        if a != int:
            print('에러발생')
        else:
            a = a**2

a = [1, 2, '4', 3]
b = count_num(a)
