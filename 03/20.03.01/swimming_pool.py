import sys
sys.stdin = open('swimming_pool.txt')

T = int(input())

def quarter_check():
    three_list = [0]
    global sum_plan
    for i in range(0, 10, 3):
        three_list[i] = plan[i] + plan[i+1] + plan[i+2]
    

def three_sum():
    three_list = []
    global sum_plan
    max_num = 0
    index_num = 0
    for i in range(10):
        three_list.append(plan[i] + plan[i+1] + plan[i+2])
        if three_list[i] >= max_num:
            max_num = three_list[i]
            index_num = i
    if max_num >= quarter:
        sum_plan += quarter
        plan[index_num], plan[index_num+1], plan[index_num+2] = 0, 0, 0
        three_list.pop(index_num)
    for i in range(len(three_list)):
        if three_list[i] > quarter:
            return three_sum()

for tc in range(T):
    day, month, quarter, year = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    sum_plan = 0
    for i in range(12):
        if day * plan[i] >= month:
            plan[i] = month
        else:
            plan[i] = day * plan[i]
    three_sum()
    for i in range(12):
        sum_plan += plan[i]
    if sum_plan >= year:
        sum_plan = year
    print('#{} {}'.format(tc+1, sum_plan))