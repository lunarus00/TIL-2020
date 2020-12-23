import sys, time

start = time.time()

sys.stdin = open('보급로.txt')

T = int(input())

for_i = [0, 1, 0, -1]
for_j = [1, 0, -1, 0]

def restore_road(y, x):
    global flag_past
    now_price = restore_price[y][x]
    for k in range(4):
        go_i = y + for_i[k]
        go_j = x + for_j[k]
        if 0 <= go_i < N and 0 <= go_j < N:
            if restore_price[go_i][go_j] == 0:
                restore_price[go_i][go_j] = now_price + road_map[go_i][go_j]
            elif restore_price[go_i][go_j] > now_price + road_map[go_i][go_j]:
                restore_price[go_i][go_j] = now_price + road_map[go_i][go_j]
                if k == 3:
                    flag_past = 1

for tc in range(T):
    N = int(input())
    road_map = []
    for i in range(N):
        road = str(input())
        road_list = []
        for j in range(len(road)):
            road_list.append(int(road[j]))
        road_map.append(road_list)
    restore_price = [[9 * (N ** 2)] * N for i in range(N)]
    restore_price[0][0] = 0
    visited = [[0] * N for i in range(N)]
    i = 0
    while i < N:
        flag = 0
        flag_past = 0
        while i < N:
            find_min = 9 * (N ** 2)
            for j in range(N):
                if restore_price[i][j] < find_min and visited[i][j] == 0:
                    find_min = road_map[i][j]
                    find_x = i
                    find_y = j
                if j == N-1:
                    if find_min == 9 * (N ** 2):
                        flag = 1
            if flag == 1:
                break
            visited[find_x][find_y] = 1
            restore_road(find_x, find_y)
        if flag_past == 0:
            i += 1
        elif flag_past == 1:
            i -= 1
    print('#{} {}'.format(tc+1, restore_price[N-1][N-1]))

print(time.time() - start)