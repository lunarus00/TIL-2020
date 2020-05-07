import sys
sys.stdin = open('dock.txt')

T = int(input())

def find_schedule(time):
    global count_truck, max_truck
    count_truck += 1
    if count_truck >= max_truck:
        max_truck = count_truck
    for j in range(N):
        if truck_list[j][0] >= time:
            find_schedule(truck_list[j][1])
            count_truck -= 1

for tc in range(T):
    N = int(input())
    truck_list = []
    for i in range(N):
        truck_list.append(list(map(int, input().split())))
    max_truck = 0
    for i in range(N):
        count_truck = 0
        find_schedule(truck_list[i][1])
    print('#{} {}'.format(tc+1, max_truck))