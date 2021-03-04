def solution(numbers):
    answer = ''
    # 9 8 7 6 5 4 3 2 10 순으로 정렬하여 사용
    str_num = []
    for i in range(len(numbers)):
        str_num.append(str(numbers[i]))
    str_num.sort(reverse = True)
    i = 0
    for i in range(1, len(str_num)):
        if len(str_num[i]) == 1:
            if int(str_num[i-1]) % 10 == 0 and int(str_num[i-1]) == int(str_num[i]) * 10:
                str_num[i-1], str_num[i] = str_num[i], str_num[i-1]
    for i in range(len(str_num)):
        answer += str_num[i]
    return answer