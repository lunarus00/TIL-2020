import sys, time

start = time.time()

sys.stdin = open('최대상금.txt')

T = int(input())

def change_num(num):
    new_num_list = []
    plus_list = []
    for index in range(len(num)):
        new_num_list.append(num[index])
    for i in range(num_length):
        if i < num_length-1:
            for j in range(i+1, num_length):
                second_list = []
                for index in range(len(new_num_list)):
                    second_list.append(new_num_list[index])
                second_list[i], second_list[j] = second_list[j], second_list[i]
                new_num = ''
                for index in range(len(second_list)):
                    new_num += second_list[index]
                plus_list.append(new_num)
                go_to_list.append(new_num)
    num_data.update({num: plus_list})

for tc in range(T):
    numbers, change = list(map(str, input().split()))
    change = int(change)
    num_list = [numbers]
    num_length = len(numbers)
    visited = []
    num_data = {}
    for k in range(change):
        go_to_list = []
        visit_sec = []
        for l in range(len(num_list)):
            if num_list[l] not in visited:
                visited.append(num_list[l])
                change_num(num_list[l])
            elif num_list[l] not in visit_sec:
                visit_sec.append(num_list[l])
                next_list = num_data[num_list[l]]
                for index in range(len(next_list)):
                    go_to_list.append(next_list[index])
        num_list = go_to_list
    max_num = 0
    for i in range(len(num_list)):
        if int(num_list[i]) > max_num:
            max_num = int(num_list[i])
    print('#{} {}'.format(tc+1, max_num))

print(time.time()-start)