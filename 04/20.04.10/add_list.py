import sys
sys.stdin = open('add_list.txt')

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    fir_list = list(map(int, input().split()))
    length = N
    for i in range(M-1):
        sec_list = list(map(int, input().split()))
        for j in range(N):
            if fir_list[j] > sec_list[0]:
                add_to_list = fir_list[j:length]
                fir_list = fir_list[0:j]
                fir_list += sec_list
                fir_list += add_to_list
                break
            elif j == N-1:
                fir_list += sec_list
        length += N
    i = 0
    final_list = []
    while i < 10:
        final_list.append(fir_list[-1-i])
        i += 1
    print('#{}'.format(tc+1), end = ' ')
    for i in range(10):
        print(final_list[i], end = ' ')
    print()