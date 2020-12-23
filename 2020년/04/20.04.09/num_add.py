import sys
sys.stdin = open('num_add.txt')

T = int(input())

for tc in range(T):
    N, M, L = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    for i in range(M):
        add_index, add_num = list(map(int, input().split()))
        num_list.insert(add_index, add_num)
    print('#{} {}'.format(tc+1, num_list[L]))