"""
소수를 검사하는 함수
소수일 경우 "소수입니다."
아닐 경우 "소수가 아닙니다."

"""

def check_prime(number):
    count_prime = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count_prime += 1
    return count_prime == 2

number = int(input())
abc = check_prime(number)
if abc == True:
    print('소수입니다.')
else:
    print('소수가 아닙니다.')