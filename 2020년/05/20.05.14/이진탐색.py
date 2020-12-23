import sys
sys.stdin = open('(5207)이진탐색_input.txt')

T = int(input())

def find_number(l, r):
    global check_direction, check_count
    m = (l + r) // 2
    m_value = find_list[m]
    if check_num > m_value:
        if check_direction != 2:
            check_direction = 2
            find_number(m+1, r)
        else:
            return
    elif check_num < m_value:
        if check_direction != 1:
            check_direction = 1
            find_number(l, m-1)
        else:
            return
    else:
        check_count += 1
        return

for tc in range(T):
    N, M = list(map(int, input().split()))
    find_list = list(map(int, input().split()))
    find_list.sort()
    number_list = list(map(int, input().split()))
    check_count = 0
    for i in range(len(number_list)):
        check_direction = 0
        check_num = number_list[i]
        find_number(0, len(find_list)-1)
    print('#{} {}'.format(tc+1, check_count))