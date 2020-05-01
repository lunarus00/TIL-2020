import sys
sys.stdin = open('bin_pass.txt')

T = int(input())

password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(T):
    N, M = list(map(int, input().split()))
    password_list = []
    for i in range(N):
        password_list.append(str(input()))
    flag = 0
    for i in range(N-1, 0, -1):
        for j in range(M-1, 0, -1):
            if password_list[i][j] == '1':
                flag = 1
                numbers = password_list[i][j-55:j+1]
                break
        if flag == 1:
            break
    i = 0
    final_list = []
    while i < 56:
        words = numbers[i:i+7]
        final_list.append(password[words])
        i += 7
    check_point = (final_list[0] + final_list[2] + final_list[4] + final_list[6]) * 3
    check_point += final_list[1] + final_list[3] + final_list[5] + final_list[7]
    if check_point % 10 == 0:
        sum_check_point = 0
        for i in range(8):
            sum_check_point += final_list[i]
        print('#{} {}'.format(tc+1, sum_check_point))
    else:
        print('#{} 0'.format(tc+1))