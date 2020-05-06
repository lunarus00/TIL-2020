import sys
sys.stdin = open('cart.txt')

T = int(input())

def find_min(num):
    global check_min, min_elec, count_position
    if check_min > min_elec:
        return
    count_position += 1
    visit[num] = 1
    if count_position == N-1:
        check_min += golf_field[num][0]
        if check_min < min_elec:
            min_elec = check_min
        check_min -= golf_field[num][0]
    else:
        for j in range(1, N):
            if visit[j] == 0:
                check_min += golf_field[num][j]
                find_min(j)
                check_min -= golf_field[num][j]
    count_position -= 1
    visit[num] = 0

for tc in range(T):
    N = int(input())
    golf_field = []
    for i in range(N):
        golf_field.append(list(map(int, input().split())))
    visit = [0] * N
    min_elec = 999999
    count_position = 0
    for i in range(1, N):
        check_min = golf_field[0][i]
        find_min(i)
    print('#{} {}'.format(tc+1, min_elec))