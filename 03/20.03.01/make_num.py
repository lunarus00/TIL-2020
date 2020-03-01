import sys
sys.stdin = open('make_num.txt')

T = int(input())

def cal_nums(n):
    global sum_nums, max_num, min_num
    for i in range(n, N-1):
        if arithmetic[i] == '+':
            sum_nums += num_list[i+1]
        elif arithmetic[i] == '-':
            sum_nums -= num_list[i+1]
        elif arithmetic[i] == '*':
            sum_nums *= num_list[i+1]
        else:
            sum_nums /= num_list[i+1]
            sum_nums = int(sum_nums)
        # if 0 < sum_nums < 1:
        #     sum_nums = 0
        cal_nums(i+1)
        if i == N-2:
            if sum_nums >= max_num:
                max_num = sum_nums
            if sum_nums <= min_num:
                min_num = sum_nums
        if arithmetic[i] == '+':
            sum_nums -= num_list[i+1]
        elif arithmetic[i] == '-':
            sum_nums += num_list[i+1]
        elif arithmetic[i] == '*':
            sum_nums /= num_list[i+1]
            int(sum_nums)
        else:
            sum_nums *= num_list[i+1]

for tc in range(T):
    N = int(input())
    cal_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    arithmetic = []
    i = 0
    while i < 4:
        if cal_list[i] == 0:
            i += 1
        else:
            if i == 0:
                arithmetic.append('+')
            elif i == 1:
                arithmetic.append('-')
            elif i == 2:
                arithmetic.append('*')
            else:
                arithmetic.append('/')
            cal_list[i] -= 1
    max_num = 0
    min_num = 999999999
    sum_nums = num_list[0]
    cal_nums(0)
    print(int(max_num - min_num))