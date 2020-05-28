import sys, time
start = time.time()

sys.stdin = open('최적경로.txt')

T = int(input())

def find_min(num):
    global check_length, min_length, count_consumer
    if check_length >= min_length:
        return
    elif count_consumer == N:
        check_length += abs(consumers[num][0] - home[0]) + abs(consumers[num][1] - home[1])
        if check_length < min_length:
            min_length = check_length
        check_length -= abs(consumers[num][0] - home[0]) + abs(consumers[num][1] - home[1])
        return
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                check_length += abs(consumers[num][0] - consumers[j][0]) + abs(consumers[num][1] - consumers[j][1])
                count_consumer += 1
                find_min(j)
                count_consumer -= 1
                check_length -= abs(consumers[num][0] - consumers[j][0]) + abs(consumers[num][1] - consumers[j][1])
                visited[j] = 0

for tc in range(T):
    N = int(input())
    location_list = list(map(int, input().split()))
    company = [location_list[0], location_list[1]]
    home = [location_list[2], location_list[3]]
    consumers = []
    for i in range(4, len(location_list), 2):
        consumers.append([location_list[i], location_list[i+1]])
    min_length = 9999999
    for i in range(N):
        visited = [0] * N
        check_length = 0
        count_consumer = 1
        check_length += abs(company[0] - consumers[i][0]) + abs(company[1] - consumers[i][1])
        visited[i] = 1
        find_min(i)
    print('#{} {}'.format(tc+1, min_length))

print(time.time()-start)