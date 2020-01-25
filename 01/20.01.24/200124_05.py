"""
1 ~ 200 사이의 정수 가운데 7의 배수이면서 5의 배수가 아닌 모든 숫자를 찾아
, 로 구분된 문자열을 구성해 출력하라

"""

numbers = ''

for i in range(1, 201):
    if i % 7 == 0:
        if i % 5 != 0:
            numbers += f'{i},'
    if i == 200:
        numbers = numbers[0:-1]

print(numbers)