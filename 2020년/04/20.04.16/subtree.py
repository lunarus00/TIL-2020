import sys
sys.stdin = open('subtree.txt')

T = int(input())

def find_node(num):
    global count_node
    count_node += 1
    if node_list[0][num] != 0:
        find_node(node_list[0][num])
    if node_list[1][num] != 0:
        find_node(node_list[1][num])

for tc in range(T):
    E, N = list(map(int, input().split()))
    node_list = [[0] * (E+2) for i in range(2)]
    input_node = list(map(int, input().split()))
    for i in range(0, len(input_node), 2):
        parent_node = input_node[i]
        child_node = input_node[i+1]
        if node_list[0][parent_node] == 0:
            node_list[0][parent_node] = child_node
        else:
            node_list[1][parent_node] = child_node
    count_node = 0
    find_node(N)
    print('#{} {}'.format(tc+1, count_node))