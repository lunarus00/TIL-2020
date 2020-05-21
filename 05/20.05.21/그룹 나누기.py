import sys, time

start = time.time()

sys.stdin = open('그룹 나누기.txt')

T = int(input())

def check_groups(number):
    for k in range(N+1):
        if node_field[number][k] == 1 or node_field[k][number] == 1:
            if visited[k] == 0:
                visited[k] = 1
                check_groups(k)

for tc in range(T):
    N, M = list(map(int, input().split()))
    line_list = list(map(int, input().split()))
    node_field = [[0] * (N+1) for i in range(N+1)]
    for i in range(0, M*2, 2):
        # print('i : ', i)
        # print(line_list[i], line_list[i+1])
        node_field[line_list[i]][line_list[i+1]] = 1
        node_field[line_list[i+1]][line_list[i]] = 1
    count_group = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            check_groups(i)
            count_group += 1
    print('#{} {}'.format(tc+1, count_group))

print(time.time()-start)