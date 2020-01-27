"""
사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환
123의 경우 1+2+3 = 6
"""

number = str(input())

numbers = list(map(lambda x: x, number))

sum_num = 0

for i in range(len(numbers)):
    sum_num += int(numbers[i])

print(sum_num)