import sys
sys.stdin = open('snake.txt')

def tail_check(y, x):                                   # 꼬리 확인용 함수 생성(현재 머리위치 y, x로 시작)
    global check_count, flag                            # 몸통 수 및 함수 종료용 변수 불러옴
    check_count += 1                                    # 첫 칸(머리)부터 count 시작
    tail_visited[y][x] = 1                              # 뱀의 위치를 어디까지 확인했는지 확인하기 위한 list
    if check_count == body+1:                           # 뱀의 현재 위치는 머리를 제외하고 체크되어 있음
        visited[y][x] = 0                               # 따라서 count가 body+1 일 경우 꼬리까지 체크됨
        flag = 1                                        # 꼬리 위치에서 뱀의 정보를 삭제(0으로 변경)
        return flag                                     # return 용 flag를 변경 후 적용
    for j in range(4):                                  # 4방향 뱀 몸통 체크
        check_i = y + for_i[j]
        check_j = x + for_j[j]
        if check_i < 1 or check_i > N or check_j < 1 or check_j > N: # list 범위 밖의 경우
            continue
        if visited[check_i][check_j] == 1 and tail_visited[check_i][check_j] == 0:  # 몸통 확인 및 체크되지 않은 경우
            tail_check(check_i, check_j)                # 해당 위치에서 꼬리 확인 함수 재호출
        if flag == 1:
            return flag
    return flag


N = int(input())                                        # 보드의 크기 N
K = int(input())                                        # 사과의 개수 K
board_apple = [[0] * (N+1) for i in range(N+1)]
for i in range(K):                                      # 사과의 위치 input
    y, x = list(map(int, input().split()))
    board_apple[y][x] = 1

L = int(input())                                        # 방향 변환 횟수 L
second_list = [0] * L
direction_list = [0] * L
for i in range(L):                                      # 초와 방향 두 개로 나눠서 input
    second_list[i], direction_list[i] = list(input().split())

for i in range(L):                                      # 초를 int로 변환
    second_list[i] = int(second_list[i])

for_i = [0, 1, 0, -1]                                   # 우, 하, 좌, 상 순으로 방향 설정
for_j = [1, 0, -1, 0]
k = 0                                                   # 시작시 오른쪽으로 이동

y = 1                                                   # 시작 위치 1, 1
x = 1

visited = [[0] * (N+1) for i in range(N+1)]             # 뱀의 현재 위치를 파악
body = 1                                                # 뱀의 현재 길이

for i in range(1, 10000):                               # 현재 흐른 시간 i
    visited[y][x] = 1                                   # 이동 전 머리의 위치 체크
    go_i = y + for_i[k]                                 # 이동할 위치
    go_j = x + for_j[k]
    if go_i == 0 or go_j == 0 or go_i > N or go_j > N:  # 이동할 위치가 벽인지 확인
        result = i                                      # 벽일 경우 현재 시간 i를 result에 넣고 종료
        break
    elif visited[go_i][go_j] == 1:                      # 이동할 위치에 뱀의 몸통이 있는지 확인
        result = i                                      # 몸통일 경우 현재 시간 i를 result에 넣고 종료
        break
    elif board_apple[go_i][go_j] == 0:                  # 사과가 없는 위치일 경우
        tail_visited = [[0] * (N+1) for i in range(N+1)]# 꼬리 삭제를 위해 0으로 이루어진 2차원 배열 생성
        check_count = 0                                 # 현재 몸통의 수 확인용 변수
        flag = 0                                        # 마지막 꼬리 확인 후 빠져나오기 위한 변수
        tail_check(go_i, go_j)                          # 꼬리 확인용 함수
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