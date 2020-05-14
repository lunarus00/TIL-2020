import sys
sys.stdin = open('(5204)병합정렬_input.txt')

T = int(input())

def merge(input_list):
    global count_right
    center = len(input_list) // 2
    left = input_list[0:center]
    right = input_list[center:len(input_list)]
    if len(left) > 1:
        left = merge(left)
    if len(right) > 1:
        right = merge(right)
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        elif left[i] == right[j]:
            result.append(right[j])
            result.append(left[i])
            i += 1
            j += 1
        else:
            result.append(left[i])
            i += 1
    if i == len(left):
        result.extend(right[j:len(right)])
    elif j == len(right):
        result.extend(left[i:len(left)])
    if left[-1] > right[-1]:
        count_right += 1
    return result

for tc in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    count_right = 0
    result_list = merge(num_list)
    print('#{} {} {}'.format(tc+1, result_list[N//2], count_right))