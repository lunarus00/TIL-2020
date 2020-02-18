import sys
sys.stdin = open('escape_ball.txt')

def ball_move(field):
    global count_move
    global success
    for k in range(4):
        go_red_i = red_i + for_i[k]
        go_red_j = red_j + for_j[k]
        go_blue_i = blue_i + for_i[k]
        go_blue_j = blue_j + for_j[k]
        while field[go_red_i][go_red_j] != '#' and field[go_blue_i][go_blue_j] != '#' and field[go_red_i][go_red_j] != 'B' and field[go_blue_i][go_blue_j] != 'R' and visited[go_red_i][go_red_j] == 0:
            if field[go_red_i][go_red_j] == '#' or field[go_red_i][go_red_j] == 'B':
                go_red_i = red_i
                go_red_j = red_j
            elif field[go_red_i][go_red_j] == 'O':
                success = 1
            else:
                go_red_i += for_i[k]
                go_red_j += for_j[k]
            if field[go_blue_i][go_blue_j] == '#' or field[go_blue_i][go_blue_j] == 'R':
                go_blue_i = blue_i
                go_blue_j = blue_j
            elif field[go_blue_i][go_blue_j] == 'O':
                success = 0
                return success
            else:
                go_blue_i += for_i[k]
                go_blue_j += for_j[k]
            visited[go_red_i][go_red_j] = 1
            field[red_i][red_j] = '.'
            field[go_red_i][go_red_j] = 'R'
            field[blue_i][blue_j] = '.'
            field[go_blue_i][go_blue_j] = 'B'
        count_move += 1
        if count_move <= 10:
            ball_move(field)
        else:
            return success
        count_move -= 1
    return success

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    field = []
    visited = [[0] * M for i in range(N)]
    for i in range(N):
        field.append(input())
    count_move = 0
    success = 0
    for_i = [-1, 1, 0, 0]
    for_j = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            if field[i][j] == "R":
                red_i = i
                red_j = j
            elif field[i][j] == 'B':
                blue_i = i
                blue_j = j
    print(ball_move(field))