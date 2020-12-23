import sys
sys.stdin = open('전기버스2.txt')

T = int(input())

def find_end(stop_num):
    global stops_count, min_count
    battery = stops[stop_num]
    if battery == 0:
        if stops_count < min_count:
            min_count = stops_count
            return
    elif stops_count >= min_count:
        return
    for i in range(1, battery+1):
        stops_count += 1
        next_stop = stop_num + i
        if next_stop < N:
            find_end(next_stop)
        stops_count -= 1

for tc in range(T):
    input_list = list(map(int, input().split()))
    N = input_list[0]
    stops = input_list[1:len(input_list)] + [0]
    stops_count = 0
    min_count = 100
    find_end(0)
    print('#{} {}'.format(tc+1, min_count-1))