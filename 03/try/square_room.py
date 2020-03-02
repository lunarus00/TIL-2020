import sys
sys.stdin = open('square_room.txt')

T = int(input())

for_i = [1, 0, -1, 0]
for_j = [0, 1, 0, -1]

def find_room(num, y, x):
    global count_room, max_room, room_number, number
    if count_room >= max_room:
        max_room = count_room
        if number < room_number:
            room_number = number
    for k in range(4):
        go_i = y + for_i[k]
        go_j = x + for_j[k]
        if 0 <= go_i < N and 0 <= go_j < N:
            now_num = square_list[go_i][go_j]
            if now_num == num + 1:
                count_room += 1
                find_room(now_num, go_i, go_j)
                count_room -= 1

for tc in range(T):
    N = int(input())
    square_list = []
    for i in range(N):
        square_list.append(list(map(int, input().split())))
    max_room = 0
    room_number = 10000
    for i in range(N):
        for j in range(N):
            count_room = 1
            number = square_list[i][j]
            find_room(number, i, j)
    print('#{} {} {}'.format(tc+1, room_number, max_room))