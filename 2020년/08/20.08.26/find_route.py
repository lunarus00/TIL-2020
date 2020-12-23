import sys, time

sys.stdin = open('find_route.txt')

start = time.time()

def routing(now_state):
    if route_map[now_state] != 0:
        find_goal.append(route_map[now_state])
    if route_map_two[now_state] != 0:
        find_goal.append(route_map_two[now_state])

for tc in range(10):

    T, line_length = list(map(int, input().split()))

    route_map = [0] * 100
    route_map_two = [0] * 100

    route_list = list(map(int, input().split()))

    for i in range(0, len(route_list), 2):
        starting_point = route_list[i]
        destination = route_list[i+1]
        if route_map[starting_point] == 0:
            route_map[starting_point] = destination
        else:
            route_map_two[starting_point] = destination

    find_goal = [0]
    flag = 0

    while len(find_goal) > 0:
        routing(find_goal[0])
        find_goal.pop(0)
        if 99 in find_goal:
            flag = 1
            break

    print('#{} {}'.format(T, flag))

print(time.time() - start)