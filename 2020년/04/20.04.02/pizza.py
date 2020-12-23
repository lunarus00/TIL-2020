import sys
sys.stdin = open("pizza.txt")

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    pizza_list = list(map(int, input().split()))
    count_list = []
    oven_pizza = []
    oven_count = []
    for i in range(1, M+1):
        count_list.append(i)
    for i in range(N):
        oven_pizza.append(pizza_list.pop(0))
        oven_count.append(count_list.pop(0))
    number = 1
    while len(oven_pizza) > 1:
        if oven_pizza[0] == 0:
            if pizza_list:
                oven_pizza[0] = pizza_list.pop(0)
                oven_count[0] = count_list.pop(0)
            else:
                oven_pizza.pop(0)
                oven_count.pop(0)
        else:
            oven_pizza.append(oven_pizza.pop(0))
            oven_count.append(oven_count.pop(0))
        if number == N:
            for i in range(len(oven_pizza)):
                oven_pizza[i] //= 2
            number = 1
        else:
            number += 1
    print("#{} {}".format(tc+1, oven_count[0]))