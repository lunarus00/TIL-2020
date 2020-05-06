import sys
sys.stdin = open('min_sum.txt')

T = int(input())

for_i = [1, 0]
for_j = [0, 1]

def find_sum(y, x):
    global min_num, check_num
    check_num += num_list[y][x]
    if check_num > min_num:
        check_num -= num_list[y][x]
        return
    if x == N - 1 and y == N - 1:
        if check_num < min_num:
            min_num = check_num
    for i in range(2):
        go_i = y + for_i[i]
        go_j = x + for_j[i]
        if 0 <= go_i < N and 0 <= go_j < N:
            find_sum(go_i, go_j)
    check_num -= num_list[y][x]

for tc in range(T):
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))
    min_num = 10 * (N**2)
    check_num = 0
    find_sum(0, 0)
    print('#{} {}'.format(tc+1, min_num))