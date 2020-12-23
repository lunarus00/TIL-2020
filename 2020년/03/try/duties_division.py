import sys
sys.stdin = open('duties_division.txt')

T = int(input())

def duties(y, x):
    global result
    check_list.append(x)
    check_duty.append(check_duty[-1] * workers[y][x] * 0.01)
    if workers[y][x] == 0 or check_duty[-1] <= result:
        return
    if y == N-1:
        if check_duty[-1] >= result:
            result = check_duty[-1]
    for k in range(N):
        if k not in check_list:
            duties(y+1, k)
            check_list.remove(k)
            if workers[y+1][k] != 0:
                check_duty.pop()

for tc in range(T):
    N = int(input())
    workers = []
    for i in range(N):
        workers.append(list(map(int, input().split())))
    result = 0
    for i in range(N):
        check_list = []
        check_duty = [1]
        duties(0, i)
    print('#{} %.6f'.format(tc+1) % (result*100))