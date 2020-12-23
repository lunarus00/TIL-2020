"""
팩토리얼을 구하는 함수
"""

def fac_num(number):
    count_fac = 1
    for i in range(1, number+1):
        count_fac = count_fac * i
    return count_fac

a = fac_num(int(input()))
print(a)