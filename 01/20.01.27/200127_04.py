"""
리스트 내포 기능을 이용하여 입력된 정수 값 5개의 평균을 구하시오
"""

sum_num = 0
numbers = []

for i in range(5):
    a = int(input())
    numbers.append(a)
    sum_num += numbers[i]

print(f'입력된 값 {numbers}의 평균은 {sum_num / 5}입니다.')