import sys, time

start = time.time()

sys.stdin = open('russia.txt')

T = int(input())

# i가 0번일 경우 흰색으로, 1 이상일 경우 흰색과 파란색
# 직전에 칠해진 색깔에 따라 다음 색을 결정
# 마지막 줄은 무조건 빨간색

def flag_color(line_num):
    global count_change, count_line, min_change, last_color
    now_change = 0
    if count_change > min_change:
        return
    if line_num == 0:
        for i in range(M):
            if flag_map[0][i] != 'W':
                now_change += 1
        count_change += now_change
        last_color = 'W'
        flag_color(line_num + 1)
    elif line_num == N-1:
        for i in range(M):
            if flag_map[0][i] != 'R':
                now_change += 1
        count_change += now_change
        if count_change < min_change:
            min_change = count_change
        count_change -= now_change
        return
    else:
        if last_color == 'W':
            for i in range(2):
                if i == 0:
                    if line_num == N - 2:
                        continue
                    for j in range(M):
                        if flag_map[line_num][j] != 'W':
                            now_change += 1
                    last_color = 'W'
                else:
                    for j in range(M):
                        if flag_map[line_num][j] != 'B':
                            now_change += 1
                    last_color = 'B'
                count_change += now_change
                flag_color(line_num + 1)
                count_change -= now_change
                now_change = 0
        else:
            for i in range(2):
                if i == 0:
                    for j in range(M):
                        if flag_map[line_num][j] != 'B':
                            now_change += 1
                    last_color = 'B'
                else:
                    for j in range(M):
                        if flag_map[line_num][j] != 'R':
                            now_change += 1
                    last_color = 'R'
                count_change += now_change
                flag_color(line_num + 1)
                count_change -= now_change
                now_change = 0

for tc in range(T):
    N, M = list(map(int, input().split()))
    flag_map = []
    for i in range(N):
        flag_map.append(input())
    count_change = 0
    count_line = 0
    flag = 0
    min_change = 4096
    last_color = ''
    flag_color(count_line)
    print('#{} {}'.format(tc+1, min_change))

print(time.time() - start)