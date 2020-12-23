import sys, time

sys.stdin = open('test_score.txt')

start_time = time.time()

T = int(input())

for tc in range(T):
    N = int(input())
    score_list = list(map(int, input().split()))

    student_score = [0]

    for i in range(N):
        for j in range(len(student_score)):
            new_num = student_score[j] + score_list[i]
            if new_num not in student_score:
                student_score.append(student_score[j] + score_list[i])

    print('#{} {}'.format(tc+1, len(student_score)))

print(time.time() - start_time)