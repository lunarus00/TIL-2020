import sys, time

start = time.time()

sys.stdin = open('공통조상.txt')

T = int(input())

def find_ancestor(first_num, second_num):
    global ancestor
    if first_num in second_ancestor_list:
        ancestor = first_num
        return
    elif second_num in first_ancestor_list:
        ancestor = second_num
        return
    else:
        next_first = 0
        next_second = 0
        for i in range(1, V+1):
            if tree_map[i][first_num] == 1:
                next_first = i
            if tree_map[i][second_num] == 1:
                next_second = i
            if next_first != 0 and next_second != 0:
                break
        first_ancestor_list.append(next_first)
        second_ancestor_list.append(next_second)

def check_tree_depth(number):
    for i in range(1, V+1):
        if tree_map[number][i] == 1:
            tree_depth.append(i)

for tc in range(T):
    V, E, first_node, second_node = list(map(int, input().split()))
    line_list = list(map(int, input().split()))
    tree_map = [[0] * (V+1) for i in range(V+1)]
    for i in range(0, len(line_list), 2):
        tree_map[line_list[i]][line_list[i+1]] = 1
    first_ancestor_list = [first_node]
    second_ancestor_list = [second_node]
    i = 0
    ancestor = 0
    while i < len(first_ancestor_list):
        first_num = first_ancestor_list[i]
        second_num = second_ancestor_list[i]
        find_ancestor(first_num, second_num)
        if ancestor != 0:
            break
        i += 1
    tree_depth = [ancestor]
    i = 0
    while i < len(tree_depth):
        check_tree_depth(tree_depth[i])
        i += 1
    print('#{} {} {}'.format(tc+1, ancestor, len(tree_depth)))

print(time.time()-start)