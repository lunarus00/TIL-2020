import sys, time

sys.stdin = open('maze_one.txt')

start_time = time.time()

for_i = [0, 1, 0, -1]
for_j = [1, 0, -1, 0]

def find_start_end():
    global start_x, start_y, end_x, end_y
    for j in range(16):
        for k in range(16):
            if maze_map[j][k] == 2:
                start_y = j
                start_x = k
            elif maze_map[j][k] == 3:
                end_y = j
                end_x = k

def find_solution(y, x):
    global result, flag
    visited[y][x] = 1
    for j in range(4):
        go_i = y + for_i[j]
        go_j = x + for_j[j]
        if 0 < go_i < 16 and 0 < go_j < 16:
            if maze_map[go_j][go_i] == 3:
                flag = 1
                return
            elif maze_map[go_j][go_i] == 0:
                if visited[go_j][go_i] == 0:
                    find_solution(go_j, go_i)
        if flag == 1:
            return

for T in range(10):
    tc = int(input())
    maze_map = []
    for i in range(16):
        maze_map.append(list(map(str, input())))
    for i in range(16):
        for j in range(16):
            maze_map[i][j] = int(maze_map[i][j])
    visited = [[0] * 16 for i in range(16)]
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    find_start_end()
    result = 0
    flag = 0
    find_solution(start_y, start_x)
    print('#{} {}'.format(tc, flag))

print(time.time() - start_time)