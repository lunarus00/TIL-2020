import sys, time

sys.stdin = open('contact.txt')

start_time = time.time()

for tc in range(10):
    L, S = list(map(int, input().split()))
    from_to = list(map(int, input().split()))
    emergency_contact = [[0] * 101 for i in range(101)]
    for i in range(0, len(from_to), 2):
        emergency_contact[from_to[i]][from_to[i+1]] = 1
    visited = [0] * 101
    count_visit = [0] * 101
    queue = [S]
    visited[S] = 1
    while queue:
        for i in range(101):
            if emergency_contact[queue[0]][i] != 0:
                if visited[i] == 0:
                    visited[i] = 1
                    queue.append(i)
                    count_visit[i] = count_visit[queue[0]] + 1
        queue.pop(0)
    max_order = 0
    max_num = 0
    for i in range(101):
        if count_visit[i] >= max_order:
            max_order = count_visit[i]
            if i > max_num:
                max_num = i
    print('#{} {}'.format(tc+1, max_num))

print(time.time() - start_time)