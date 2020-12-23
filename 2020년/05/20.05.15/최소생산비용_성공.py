import sys
sys.stdin = open('최소생산비용.txt')

T = int(input())

def find_sum(num):
    global count_sum, min_price, check_pactory
    if count_sum >= min_price:
        return
    elif check_pactory == N:
        if count_sum < min_price:
            min_price = count_sum
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            count_sum += pactory[j][num+1]
            check_pactory += 1
            find_sum(num+1)
            check_pactory -= 1
            count_sum -= pactory[j][num+1]
            visited[j] = 0

for tc in range(T):
    N = int(input())
    pactory = []
    for i in range(N):
        pactory.append(list(map(int, input().split())))
    min_price = 2000
    visited = [0] * N
    for i in range(N):
        count_sum = pactory[i][0]
        check_pactory = 1
        visited[i] = 1
        find_sum(0)
        visited[i] = 0
    print('#{} {}'.format(tc+1, min_price))