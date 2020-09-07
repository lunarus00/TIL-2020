import sys, time

sys.stdin = open('dongchul.txt')

start_time = time.time()

def find_max():
    global count_num, max_percent, check_sum
    if count_num == N:
        if check_sum > max_percent:
            max_percent = check_sum
    else:
        for j in range(N):
            if visited_person[j] == 0:
                visited_person[j] = 1
                for k in range(N):
                    if visited_project[k] == 0:
                        visited_project[k] = 1
                        count_num += 1
                        if person_list[j][k] != 0:
                            check_sum *= person_list[j][k] / 100
                        find_max()
                        if person_list[j][k] != 0:
                            check_sum /= person_list[j][k] / 100
                        count_num -= 1
                        visited_project[k] = 0
                visited_person[j] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    person_list = []
    for i in range(N):
        person_list.append(list(map(int, input().split())))

    visited_person = [0] * N
    visited_project = [0] * N

    max_percent = 0

    for i in range(N):
        count_num = 1
        check_sum = person_list[0][i] / 100
        visited_person[0] = 1
        visited_project[i] = 1
        find_max()
        visited_person[0] = 0
        visited_project[i] = 0

    max_percent = max_percent * 100

    print('#{}'.format(tc+1), end = ' ')
    print('%.6f' % max_percent)

print(time.time()-start_time)