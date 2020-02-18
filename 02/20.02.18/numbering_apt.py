import sys
sys.stdin = open('numbering_apt.txt')

N = int(input())
fir_input = []

for_i = [-1, 1, 0, 0]
for_j = [0, 0, -1, 1]

def numbering(y, x):
    global count_apt
    count_apt += 1
    apt_list[y][x] = 0
    for k in range(4):
        go_i = y + for_i[k]
        go_j = x + for_j[k]
        while 0 <= go_i < N and 0 <= go_j < N:
            if apt_list[go_i][go_j] == 1:
                numbering(go_i, go_j)
            else:
                break

for i in range(N):
    fir_input.append(input())

apt_list = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        apt_list[i][j] = int(fir_input[i][j])

count_list = []

for i in range(N):
    for j in range(N):
        if apt_list[i][j] == 1:
            count_apt = 0
            numbering(i, j)
            count_list.append(count_apt)

for i in range(len(count_list)):
    for j in range(i, len(count_list)):
        if count_list[j] < count_list[i]:
            count_list[i], count_list[j] = count_list[j], count_list[i]

print(len(count_list))
for i in range(len(count_list)):
    print(count_list[i])