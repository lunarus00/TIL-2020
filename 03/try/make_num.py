import sys
sys.stdin = open('make_num.txt')

def cal_nums(n):
    global max_num, min_num, check_cal
    if n == N-1:
        if check_cal >= max_num:
            max_num = check_cal
        elif check_cal <= min_num:
            min_num = check_cal
    else:
        for i in range(len(operation)):
            if i not in check_list:
                check_list.append(i)
                if operation[i] == '+':
                    check_cal += num_list[n+1]
                    cal_nums(n+1)
                    check_cal -= num_list[n+1]
                elif operation[i] == '-':
                    check_cal -= num_list[n+1]
                    cal_nums(n+1)
                    check_cal += num_list[n+1]
                elif operation[i] == '*':
                    check_cal *= num_list[n+1]
                    cal_nums(n+1)
                    check_cal /= num_list[n+1]
                    check_cal = int(check_cal)
                elif operation[i] == '/':
                    check_cal /= num_list[n+1]
                    check_cal = int(check_cal)
                    cal_nums(n+1)
                    check_cal *= num_list[n+1]
                check_list.remove(i)

T = int(input())

for tc in range(T):
    N = int(input())
    cal_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    operation = []
    check_list = []
    max_num = -100000000
    min_num = 100000000
    i = 0
    while i < 4:
        if cal_list[i] == 0:
            i += 1
            continue
        else:
            if i == 0:
                operation.append('+')
                cal_list[i] -= 1
            elif i == 1:
                operation.append('-')
                cal_list[i] -= 1
            elif i == 2:
                operation.append('*')
                cal_list[i] -= 1
            elif i == 3:
                operation.append('/')
                cal_list[i] -= 1
    check_cal = num_list[0]
    cal_nums(0)
    print(int(max_num - min_num))