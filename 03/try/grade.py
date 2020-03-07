import sys
sys.stdin = open('grade.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    grade_list = list(map(int, input().split()))
    check_list = []
    count_grade = 1
    for i in range(1<<N):
        sum_grade = 0
        for j in range(N):
            if i & (1<<j):
                sum_grade += grade_list[j]
                if sum_grade not in check_list:
                    count_grade += 1
                    check_list.append(sum_grade)
    print('#{} {}'.format(tc+1, count_grade))