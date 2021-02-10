import itertools
def solution(numbers):
    answer = 0
    length = len(numbers)
    check_list = []
    num_list = []
    for i in range(1, length+1):
        temp = list(map(''.join, itertools.permutations(numbers, i)))
        check_list.extend(temp)
    for i in range(len(check_list)):
        num_list.append(int(check_list[i]))
    num_list.sort()
    i = 0
    while i < len(num_list)-1:
        if num_list[i] == 0 or num_list[i] == 1:
            num_list.remove(num_list[i])
            continue
        check_num = num_list[i]
        j = i + 1
        while j < len(num_list):
            if num_list[j] == check_num:
                num_list.remove(num_list[j])
            else:
                j += 1
        i += 1
    i = 0
    while i < len(num_list):
        check_num = num_list[i]
        flag = 0
        for j in range(2, check_num):
            if check_num % j == 0:
                num_list.remove(check_num)
                flag = 1
                break
        if flag == 0:
            i += 1
    answer = len(num_list)
    return answer