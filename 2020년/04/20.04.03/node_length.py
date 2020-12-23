import sys
sys.stdin = open('node_length.txt')

T = int(input())

def find_goal(number):
    global G, flag, count_length
    for i in range(1, V+1):
        if node_list[number][i] == 1:
            if i == G:
                count_length = visited[number]
                flag = 1
                return
            elif visited[i] == 0:
                check_point.append(i)
                visited[i] = visited[number] + 1

for tc in range(T):
    V, E = list(map(int, input().split()))
    node_list = [[0] * (V+1) for i in range(V+1)]
    visited = [0] * (V+1)
    check_point = []
    for i in range(E):
        num1, num2 = list(map(int, input().split()))
        node_list[num1][num2] = 1
        node_list[num2][num1] = 1
    S, G = list(map(int, input().split()))
    flag = 0
    check_point.append(S)
    count_length = 0
    visited[S] = 1
    while len(check_point) >= 1:
        number = check_point.pop(0)
        find_goal(number)
        if flag == 1:
            break
    print("#{} {}".format(tc+1, count_length))