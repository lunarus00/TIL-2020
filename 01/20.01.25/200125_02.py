"""
1부터 100까지의 숫자를 for문과 range함수를 이용해 출력하시오

for i in range(1, 101):
    print(i)


1부터 100까지의 숫자 중 짝수를 for문을 이용해 짝수만 출력

for i in range(2,101,2):
    print(i)


1부터 100까지의 숫자 중 3의 배수의 총합을 for문을 이용해 출력

"""

sum_count = 0

for i in range(1, 101):
    if i % 3 == 0:
        sum_count += i

print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {sum_count}')

