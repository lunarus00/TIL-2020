import sys
sys.stdin = open('swimming_pool.txt')

T = int(input())

def three_sum(n):
    global sum_plan, check_sum
    if n >= 12:
        if check_sum < sum_plan:
            sum_plan = check_sum
    else:
        check_sum += quarter
        three_sum(n+3)
        check_sum -= quarter
        check_sum += plan[n]
        three_sum(n+1)
        check_sum -= plan[n]

for tc in range(T):
    day, month, quarter, year = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    for i in range(12):
        if day * plan[i] >= month:
            plan[i] = month
        else:
            plan[i] = day * plan[i]
    sum_plan = 3000 * 365
    check_sum = 0
    three_sum(0)
    if sum_plan >= year:
        sum_plan = year
    print('#{} {}'.format(tc+1, sum_plan))