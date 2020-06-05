import sys, time

start = time.time()

sys.stdin = open('장훈이.txt')

T = int(input())

def find_height(num):
    global min_height, check_height
    check_height += assistants[num]
    if check_height >= min_height:
        check_height -= assistants[num]
        return
    if B <= check_height < min_height:
        min_height = check_height
        check_height -= assistants[num]
        return
    else:
        for k in range(num+1, N):
            find_height(k)
    check_height -= assistants[num]


for tc in range(T):
    N, B = list(map(int, input().split()))
    assistants = list(map(int, input().split()))
    min_height = sum(assistants)
    check_height = 0
    for i in range(N):
        find_height(i)
    print('#{} {}'.format(tc+1, min_height - B))

print(time.time()-start)