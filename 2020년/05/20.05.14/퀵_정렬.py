import sys
sys.stdin = open('퀵_정렬.txt')

T = int(input())

def quick_sort(min_number, max_number):
    i = min_number
    j = max_number
    if i >= j:
        return
    elif i == j - 1:
        if number_list[i] < number_list[j] or number_list[i] == number_list[j]:
            return
    center = number_list[(i + j) // 2]
    while i < j:
        if number_list[i] < center:
            i += 1
        elif number_list[j] > center:
            j -= 1
        elif number_list[i] == number_list[j]:
            break
        else:
            number_list[i], number_list[j] = number_list[j], number_list[i]
    quick_sort(min_number, j)
    quick_sort(j, max_number)

for tc in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    quick_sort(0, N-1)
    print('#{} {}'.format(tc+1, number_list[N//2]))