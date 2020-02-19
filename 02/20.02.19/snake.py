import sys
sys.stdin = open('snake.txt')

def check_tail(y, x):
    global check_count, flag
    check_count += 1
    vi_visited[y][x] = 1
    if check_count == body+1:
        visited[y][x] = 0
        flag = 1
        return flag
    for j in range(4):
        check_i = y + for_i[j]
        check_j = x + for_j[j]
        if check_i > N or check_j > N:
            continue
        if visited[check_i][check_j] == 1 and vi_visited[check_i][check_j] == 0:
            check_tail(check_i, check_j)
        if flag == 1:
            return flag
    return flag


N = int(input())
K = int(input())
board_apple = [[0] * (N+1) for i in range(N+1)]
for i in range(K):
    y, x = list(map(int, input().split()))
    board_apple[y][x] = 1

L = int(input())
second_list = [0] * L
direction_list = [0] * L
for i in range(L):
    second_list[i], direction_list[i] = list(input().split())

for i in range(L):
    second_list[i] = int(second_list[i])

for_i = [0, 1, 0, -1]
for_j = [1, 0, -1, 0]
k = 0

y = 1
x = 1

visited = [[0] * (N+1) for i in range(N+1)]
body = 1

for i in range(1, 10000):
    visited[y][x] = 1
    go_i = y + for_i[k]
    go_j = x + for_j[k]
    if go_i == 0 or go_j == 0 or go_i > N or go_j > N:
        result = i
        break
    elif visited[go_i][go_j] == 1:
        result = i
        break
    elif board_apple[go_i][go_j] == 0:
        vi_visited = [[0] * (N+1) for i in range(N+1)]
        check_count = 0
        flag = 0
        check_tail(go_i, go_j)
    elif board_apple[go_i][go_j] == 1:
        body += 1
        board_apple[go_i][go_j] = 0
    if i in second_list:
        num = second_list.index(i)
        if direction_list[num] == 'L':
            k -= 1
            if k < 0:
                k = 3
        elif direction_list[num] == 'D':
            k += 1
            if k > 3:
                k = 0
    y = go_i
    x = go_j
print(result)