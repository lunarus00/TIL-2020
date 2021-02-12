def solution(array, commands):
    answer = []
    find_list = []
    for i in range(len(commands)):
        check_list = []
        for j in range(commands[i][0]-1, commands[i][1]):
            check_list.append(array[j])
        check_list.sort()
        find_list.append(check_list)
    for i in range(len(find_list)):
        answer.append(find_list[i][commands[i][2]-1])
    return answer