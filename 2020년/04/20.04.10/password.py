import sys
sys.stdin = open('password.txt')

T = int(input())

for tc in range(T):
    N, M, K = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    k = 0
    m = 0
    while k < K:
        m += M
        k += 1
        if m > len(num_list):
            m -= len(num_list)
        elif m == len(num_list):
            num_list.insert(m, 0)
            num_list[m] = num_list[m-1] + num_list[0]
            continue
        num_list.insert(m, 0)
        num_list[m] = num_list[m-1] + num_list[m+1]
    num_list = num_list[::-1]
    print('#{}'.format(tc+1), end = ' ')
    for i in range(len(num_list)):
        print(num_list[i], end = ' ')
        if i >= 9:
            break
    print()