"""
임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하라


number = int(input())

for i in range(1, number + 1):
    if number%i == 0:
        print(f'{i}(은)는 {number}의 약수입니다.')


약수가 2개일 경우 소수임을 나타내시오.
"""

number = int(input())

count_num = 0

for i in range(1, number + 1):
    if number%i == 0:
        print(f'{i}(은)는 {number}의 약수입니다.')
        count_num += 1

if count_num == 2:
    print(f'{number}(은)는 1과 {number}로만 나눌 수 있는 소수입니다.')