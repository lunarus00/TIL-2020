import sys, time

start = time.time()

sys.stdin = open('연산.txt')

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    flag = 0
    second_list = [N]
    dump = []
    count_cal = 0
    while flag == 0:
        number_list = second_list
        second_list = []
        for number in number_list:
            if number in dump:
                continue
            cal_list = [number + 1, number - 1, number * 2, number - 10]
            if M in cal_list:
                flag = 1
                break
            else:
                for i in range(4):
                    if cal_list[i] not in dump and cal_list[i] > 0 and cal_list[i] <= 1000000:
                        second_list.append(cal_list[i])
            dump.append(number)
        number_list = []
        count_cal += 1
    print('#{} {}'.format(tc+1, count_cal))
print("time : ", time.time() -start)