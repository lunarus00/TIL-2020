"""
가변형 인자를 전달받아 가장 큰 값을 반환하는 함수 정의

출력
max(3, 5, 4, 1, 8, 10, 2) => 10
"""

def maximum(*args):
    max = 0
    for item in args:
        if item > max:
            max = item
    return max

max_number = maximum(3, 5, 4, 1, 8, 10, 2)
print(f'max(3, 5, 4, 1, 8, 10, 2) => {max_number}')
