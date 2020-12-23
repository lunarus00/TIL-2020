import sys
sys.stdin = open('binary.txt')

T = int(input())

for tc in range(T):
    N, number = list(map(str, input().split()))
    b_num = ''
    for i in range(len(number)):
        sample_num = bin(int(number[i], 16))
        sample_num = sample_num[2:6]
        while len(b_num) + len(sample_num) < (i+1) * 4:
            b_num += '0'
        b_num += sample_num
    print('#{} {}'.format(tc+1, b_num))