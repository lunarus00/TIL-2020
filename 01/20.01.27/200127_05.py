"""
정수를 입력하면 약수를 리스트에 추가해 출력하라

numbers = []
number = int(input())

for i in range(1, number + 1):
    if number % i == 0:
        numbers.append(i)

print(numbers)


정수를 입력하면 리스트 내포를 이용해 약수 리스트를 출력하라
"""

number = int(input())
numbers = [i for i in range(1, number + 1) if number % i == 0]
print(numbers)