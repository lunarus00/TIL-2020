import sys
sys.stdin = open('sequence_edit.txt')

T = int(input())

for tc in range(T):
    N, M, L = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    for i in range(M):
        edit_input = list(map(str, input().split()))
        if len(edit_input) == 2:
            num_list.pop(int(edit_input[1]))
        elif edit_input[0] == 'I':
            num_list.insert(int(edit_input[1]), int(edit_input[2]))
        else:
            num_list[int(edit_input[1])] = int(edit_input[2])
    print('#{}'.format(tc+1), end = ' ')
    if len(num_list) >= L-1:
        print('{}'.format(num_list[L]))
    else:
        print(-1)