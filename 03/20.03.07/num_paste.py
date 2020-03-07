import sys
sys.stdin = open('num_paste.txt')

T = int(input())

for_i = [0, 1, 0, -1]
for_j = [1, 0, -1, 0]

def find_nums(i, j):
    global check_nums, check_count, count_nums
    if check_count == 7:
        if check_nums not in check_list:
            check_list.append(check_nums)
            count_nums += 1
            return
        else:
            return
    for k in range(4):
        go_i = i + for_i[k]
        go_j = j + for_j[k]
        if 0 <= go_i < 4 and 0 <= go_j < 4:
            check_count += 1
            check_nums += matrix[go_i][go_j]
            find_nums(go_i, go_j)
            check_count -= 1
            check_nums = check_nums[:-1]

for tc in range(T):
    matrix = []
    for i in range(4):
        matrix.append(list(map(str, input().split())))
    count_nums = 0
    check_list = []
    fir_num = []
    sec_visited = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            check_count = 1
            check_nums = matrix[i][j]
            fir_num.append(matrix[i][j])
            find_nums(i, j)
    print('#{} {}'.format(tc+1, count_nums))