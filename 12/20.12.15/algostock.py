import sys

sys.stdin = open('algostock.txt')

T = int(input())

for tc in range(T):
    default_money, month_plus = list(map(int, input().split()))
    N, L = list(map(int, input().split()))
    stock_list = []
    for i in range(N):
        stock_list.append(list(map(int, input().split())))

    now_money = default_money
    base_money = now_money + (month_plus * L)

    for i in range(L + 1):
        plus_money = 0
        month_list = []
        if i == L:
            break
        while now_money > 0:
            check_money = 0
            check_month = 0
            for j in range(N):
                if j in month_list:
                    continue
                check_val = stock_list[j][i + 1] - stock_list[j][i]
                if check_money < check_val:
                    check_money = check_val
                    check_month = j
                elif check_money == check_val:
                    if stock_list[check_month][i] > stock_list[j][i]:
                        check_money = check_val
                        check_month = j
            if check_money == 0:
                break
            while now_money - stock_list[check_month][i] >= 0:
                now_money -= stock_list[check_month][i]
                plus_money += stock_list[check_month][i + 1]
            month_list.append(check_month)
            if len(month_list) == N:
                break
        now_money += plus_money + month_plus

    print(('#{} {}').format(tc+1, now_money-base_money))