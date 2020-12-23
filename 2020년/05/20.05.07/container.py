import sys
sys.stdin = open('container.txt')

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    freights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    total_freights = 0
    for i in range(len(trucks)):
        loaded_truck = 0
        flag = 0
        for j in range(len(freights)):
            if trucks[i] >= freights[j] and loaded_truck < freights[j]:
                loaded_truck = freights[j]
                check_freight = j
                flag = 1
        if flag == 0:
            continue
        total_freights += loaded_truck
        if len(freights) == 0:
            break
        freights.pop(check_freight)
    print('#{} {}'.format(tc+1, total_freights))
