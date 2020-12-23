"""
2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력
리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력
"""

numbers = input()

list_number = numbers.split(', ')

int_num = list(map(int, list_number))

list_num = []

for i in range(int_num[0]):
    list_plus = []
    for j in range(int_num[1]):
        list_plus.append(i * j)
    list_num.append(list_plus)

print(list_num)