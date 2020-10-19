import sys, time

sys.stdin = open('음식배달.txt')

start_time = time.time()

def find_food(number):
    global min_val, check_val
    y_num = number[0]
    x_num = number[1]
    check_val += map_list[y_num][x_num]
    for k in range(1, N):
        for l in range(1, N):
            if map_list[k][l] == 1:
                value = abs(k-y_num) + abs(l-x_num)
                if visited[k][l] > value or visited[k][l] == 0:
                    check_val -= visited[k][l]
                    visited[k][l] = value
                    check_val += value

def johab(num, count_num):
    global check_val, min_val
    if check_val >= min_val:
        return
    elif count_num == 0:
        if check_val < min_val:
            min_val = check_val
    for j in range(num, food_length):
        find_food(food_list[j])
        johab(j+1, count_num-1)

T = int(input())

for tc in range(T):
    N = int(input())
    map_list = []
    for i in range(N):
        map_list.append(list(map(int, input().split())))
    food_list = []
    for i in range(1, N):
        for j in range(1, N):
            if map_list[i][j] >= 2:
                food_list.append((i, j))
    food_length = len(food_list)
    min_val = 262144
    for i in range(food_length):
        check_val = 0
        visited = [[0] * N for j in range(N)]
        johab(i, food_length-i)

    print('#{} {}'.format(tc+1, min_val))

print(start_time - time.time())