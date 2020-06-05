import sys, time

start = time.time()

sys.stdin = open('하나로.txt')

T = int(input())

def find_routes(num):
    global count_islands, total_length, check_index
    for i in range(N):
        if visited[i] == 0:
            length = (island_X[num] - island_X[i]) ** 2 + (island_Y[num] - island_Y[i]) ** 2
            if lines[i] == 0:
                lines[i] = length
            elif length < lines[i]:
                lines[i] = length
    min_length = 0
    for i in range(N):
        if visited[i] == 0:
            if min_length == 0:
                min_length = lines[i]
                check_index = i
            elif lines[i] < min_length:
                min_length = lines[i]
                check_index = i
    total_length += min_length
    count_islands += 1
    visited[check_index] = 1

for tc in range(T):
    N = int(input())
    island_X = list(map(int, input().split()))
    island_Y = list(map(int, input().split()))
    E = float(input())
    visited = [0] * N
    lines = [0] * N
    visited[0] = 1
    count_islands = 0
    total_length = 0
    check_index = 0
    while count_islands < N-1:
        find_routes(check_index)
    print('#{} {}'.format(tc+1, round(total_length*E)))

print(time.time()-start)