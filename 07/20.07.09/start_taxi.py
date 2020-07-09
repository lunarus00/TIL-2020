import sys, time

sys.stdin = open('start_taxi.txt')

start = time.time()

N, M, Fuel = list(map(int, input().split()))

field = [0]

for_i = [0, 1, 0, -1]
for_j = [1, 0, -1, 0]

def find_passenger(now_taxi_y, now_taxi_x):
    for k in range(4):
        go_i = now_taxi_y + for_i[k]
        go_j = now_taxi_x + for_j[k]
        if 0 < go_i <= N and 0 < go_j <= N:
            if take_passengers[go_i][go_j] == 0 and field[go_i][go_j] == 0:
                take_passengers[go_i][go_j] = take_passengers[now_taxi_y][now_taxi_x] + 1
                taxis.append(go_i)
                taxis.append(go_j)

def find_gall(now_taxi_y, now_taxi_x):
    for k in range(4):
        go_i = now_taxi_y + for_i[k]
        go_j = now_taxi_x + for_j[k]
        if 0 < go_i <= N and 0 < go_j <= N:
            if take_passengers[go_i][go_j] == 0 and field[go_i][go_j] == 0:
                take_passengers[go_i][go_j] = take_passengers[now_taxi_y][now_taxi_x] + 1
                taxis.append(go_i)
                taxis.append(go_j)


for i in range(1, N+1):
    field.append(list(map(int, input().split())))
    field[i].insert(0, 0)

taxi = list(map(int, input().split()))

passengers = [0]

for i in range(1, M+1):
    passengers.append(list(map(int, input().split())))

visited = [0] * (M+1)

num_of_passenger = M+1

while M > 0:
    flag = 0
    taxis = [taxi[0], taxi[1]]

    take_passengers = [[0] * (N+1) for i in range(N+1)]

    while taxis:
        find_passenger(taxis[0], taxis[1])
        taxis.pop(0)
        taxis.pop(0)

    passenger = 0
    min_length = 500

    for i in range(1, num_of_passenger):
        if visited[i] == 0:
            if take_passengers[passengers[i][0]][passengers[i][1]] < min_length:
                min_length = take_passengers[passengers[i][0]][passengers[i][1]]
                passenger = i
    if min_length == 0:
        Fuel = -1
        flag = 1
        break
    visited[passenger] = 1
    # print(visited)
    Fuel -= take_passengers[passengers[passenger][0]][passengers[passenger][1]]
    # print('손님위치', Fuel)
    if Fuel < 0:
        Fuel = -1
        flag = 1
    else:
        Fuel += take_passengers[passengers[passenger][2]][passengers[passenger][3]] * 2
        taxi = [passengers[passenger][2], passengers[passenger][3]]
    if flag == 1:
        break

    taxis = [passengers[passenger][0], passengers[passenger][1]]

    take_passengers = [[0] * (N+1) for i in range(N+1)]

    while taxis:
        find_gall(taxis[0], taxis[1])
        taxis.pop(0)
        taxis.pop(0)

    Fuel -= take_passengers[passengers[passenger][2]][passengers[passenger][3]]
    # print('목적지위치', Fuel)
    if Fuel < 0:
        Fuel = -1
        flag = 1
    else:
        Fuel += take_passengers[passengers[passenger][2]][passengers[passenger][3]] * 2
        taxi = [passengers[passenger][2], passengers[passenger][3]]
    # print('연료보충', Fuel)
    if flag == 1:
        break
    M -= 1

print(Fuel)

print(time.time()-start)