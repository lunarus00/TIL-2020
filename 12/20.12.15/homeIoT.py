import sys

sys.stdin = open('homeIoT.txt')

T = int(input())

def search():
    global num_IoT, num_AP
    for i in range(N):
        for j in range(N):
            if house[i][j] == 1:
                IoT_list.append([1, i, j])
                num_IoT += 1
            elif house[i][j] == 2:
                IoT_list.append([2, i, j])
                num_IoT += 1
            elif house[i][j] == 3:
                IoT_list.append([3, i, j])
                num_IoT += 1
            elif house[i][j] == 9:
                AP_list.append([i, j])
                num_AP += 1

def check_field(y, x, AP_number):
    check_house = [[0] * N for j in range(N)]
    for j in range(N):
        for k in range(N):
            if abs(y-j) + abs(x-k) <= range_ap:
                check_house[j][k] = 1
    for j in range(num_IoT):
        find_IoT(IoT_list[j][0], IoT_list[j][1], IoT_list[j][2], AP_number, j, check_house)

def find_IoT(IoT_range, IoT_y, IoT_x, AP_number, IoT_number, check_house):
    flag = 0
    IoT_house = [[0] * N for k in range(N)]
    for k in range(N):
        for l in range(N):
            if abs(IoT_y-k) + abs(IoT_x-l) <= IoT_range:
                IoT_house[k][l] = 1
    for k in range(N):
        for l in range(N):
            if check_house[k][l] == 1 and IoT_house[k][l] == 1:
                check_IoT[IoT_number].append(AP_number)
                flag = 1
                break
        if flag == 1:
            break

for tc in range(T):
    N, range_ap = list(map(int, input().split()))
    house = []
    for i in range(N):
        house.append(list(map(int, input().split())))

    IoT_list = []
    AP_list = []
    num_IoT, num_AP = 0, 0
    search()
    check_IoT = [[] * num_IoT for i in range(num_IoT)]
    for i in range(num_AP):
        check_field(AP_list[i][0], AP_list[i][1], i)

    flag = 0
    count_AP = 0
    used_AP = []
    for i in range(num_IoT):
        if check_IoT[i]:
            if len(check_IoT[i]) == 1:
                if check_IoT[i][0] not in used_AP:
                    count_AP += 1
                    used_AP.append(check_IoT[i][0])
        else:
            flag = -1
            break

    for i in range(len(check_IoT)):
        check_num = -1
        for j in range(len(check_IoT[i])):
            if check_IoT[i][j] not in used_AP:
                check_num = check_IoT[i][j]
            else:
                check_num = -1
                break
        if check_num != -1:
            count_AP += 1
            used_AP.append(check_num)

    if count_AP > 5:
        flag = -1

    if flag == -1:
        print('#{} {}'.format(tc+1, flag))
    else:
        print('#{} {}'.format(tc+1, count_AP))