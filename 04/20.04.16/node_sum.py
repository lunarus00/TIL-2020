import sys
sys.stdin = open('node_sum.txt')

T = int(input())

def sum_node(number):
    if number == 0:
        return 0
    if node_list[2][number] == 0:
        node_list[2][number] = sum_node(node_list[0][number]) + sum_node((node_list[1][number]))
    return node_list[2][number]

for tc in range(T):
    N, M, L = list(map(int, input().split()))
    node_list = [[0] * (N+1) for i in range(3)]
    i = 1
    j = 2
    while j <= N:
        node_list[0][i] = j
        if j+1 <= N:
            node_list[1][i] = j+1
        j += 2
        i += 1
    i = 0
    while i < M:
        node_num, value = list(map(int, input().split()))
        node_list[2][node_num] = value
        i += 1
    print('#{} {}'.format(tc+1, sum_node(L)))