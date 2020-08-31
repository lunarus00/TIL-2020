import sys, time

sys.stdin = open('highest_shelf.txt')

start_time = time.time()

T = int(input())

def find_high(num):
    global check_height, min_height
    check_height += member_list[num]
    if check_height < min_height and check_height >= B:
        min_height = check_height
    else:
        if check_height >= min_height:
            return
        else:
            for j in range(num+1, N):
                find_high(j)
                check_height -= member_list[j]

for tc in range(T):
    N, B = list(map(int, input().split()))
    member_list = list(map(int, input().split()))
    min_height = sum(member_list)
    for i in range(N):
        check_height = 0
        find_high(i)
    print('#{} {}'.format(tc+1, min_height - B))

print(start_time - time.time())