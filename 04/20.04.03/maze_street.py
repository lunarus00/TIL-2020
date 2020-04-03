import sys
sys.stdin = open('maze_street.txt')

T = int(input())

for_i = [0, 1, 0, -1]
for_j = [1, 0, -1, 0]

def find_maze(y, x):
    global flag, count_street
    for i in range(4):
        go_i = y + for_i[i]
        go_j = x + for_j[i]
        if 0 <= go_i < N and 0 <= go_j < N:
            if visited[go_i][go_j] == 0:
                if maze[go_i][go_j] == 3:
                    flag = 1
                    count_street = visited[y][x]
                    return
                elif maze[go_i][go_j] == 0:
                    visited[go_i][go_j] = visited[y][x] + 1
                    check_point.append(go_i)
                    check_point.append(go_j)
    if flag == 1:
        return

for tc in range(T):
    N = int(input())
    check_list = []
    maze = [[0] * N for i in range(N)]
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        check_list.append(str(input()))
        for j in range(N):
            maze[i][j] = int(check_list[i][j])
            if maze[i][j] == 2:
                check_point = [i, j]
                visited[i][j] = 1
    flag = 0
    count_street = 0
    while len(check_point) >= 1:
        find_maze(check_point.pop(0), check_point.pop(0))
        if flag == 1:
            break
    print('#{}'.format(tc+1), end = ' ')
    if flag == 1:
        print(count_street-1)
    else:
        print(0)