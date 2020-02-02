"""
1000명의 수학 성적으로 통계 자료
최빈수를 출력(가장 자주 등장하는 값)
단, 최빈수가 여러 개 일 때는 가장 큰 점수 출력
"""

T = int(input())

for tc in range(T):
    N = int(input())
    score_list = list(map(int, input().split()))
    count_list = []
    max_num = 0
    print_num = 0
    for i in range(0, 101):
        count_list.append(score_list.count(i))
        if count_list[i] > max_num:
            max_num = count_list[i]
            print_num = i
    print(f'#{tc+1} {max_num}')