"""
숫자에 대한 제곱을 구하는 함수
숫자를 ,로 구분하여 입력
"""

def square_num(number):
    square1 = number[0] ** 2
    square2 = number[1] ** 2
    print(f'square({number[0]}) => {square1}')
    print(f'square({number[1]}) => {square2}')

s = input()

number = list(map(int, s.split(',')))

square_num(number)