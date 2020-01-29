"""
콤마(,)로 구분해 여러 원의 반지름을 입력받아
이들에 대한 원의 둘레를 계산해 출력
"""

import math

numbers = input()

list_number = numbers.split(', ')

pri_word = ''

for i in range(len(list_number)):
    list_number[i] = int(list_number[i])

for i in range(len(list_number)):
    pri_word += '%.2f'%(list_number[i] * math.pi * 2)
    pri_word += ', '

print(pri_word[:-2])