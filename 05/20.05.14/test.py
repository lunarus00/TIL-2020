import sys
sys.stdin = open('퀵_정렬.txt')

T = int(input())

def quick_sort(number_list):
    # print(number_list)

    if len(number_list) <= 1:
        return number_list

    pivot = number_list[len(number_list) // 2]
    small = []
    big = []
    same = []

    for elem in number_list:
        if elem < pivot:
            small.append(elem)
        elif elem > pivot:
            big.append(elem)
        elif elem == pivot:
            same.append(elem)

    return quick_sort(small) + same + quick_sort(big)

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quick_sort(arr)
    print('#{} {}'.format(tc + 1, arr[N // 2]))