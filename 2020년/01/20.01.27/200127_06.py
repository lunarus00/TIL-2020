"""
[1, 3, 11, 15, 23, 28, 37, 52, 85, 100] 와 같은 리스트 객체
짝수만 항목으로 가지는 리스트 객체를 생성
"""

numbers = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
number = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        number.append(numbers[i])

print(number)