import sys
sys.stdin = open('최소생산비용.txt')

T = int(input())

def find_produce(y, x):
    global min_price, check_price, count_pactory
    visited[y] = 1
    product[x] = 1
    check_price += pactory[y][x]
    if check_price >= min_price:
        check_price -= pactory[y][x]
        visited[y] = 0
        product[x] = 0
        return
    elif count_pactory == N:
        if check_price < min_price:
            min_price = check_price
            check_price -= pactory[y][x]
            visited[y] = 0
            product[x] = 0
            return
    for k in range(N):
        if visited[k] == 0:
            for l in range(N):
                if product[l] == 0:
                    count_pactory += 1
                    find_produce(k, l)
                    count_pactory -= 1
    check_price -= pactory[y][x]
    visited[y] = 0
    product[x] = 0

for tc in range(T):
    N = int(input())
    pactory = []
    for i in range(N):
        pactory.append(list(map(int, input().split())))
    min_price = 2000
    check_price = 0
    count_pactory = 0
    visited = [0] * N
    product = [0] * N
    for i in range(N):
        for j in range(N):
            count_pactory += 1
            find_produce(i, j)
            count_pactory -= 1
    print('#{} {}'.format(tc+1, min_price))