"""
한 학생의 국어, 수학 점수를 튜플로 저장
이 튜플을 항목으로 갖는 리스트 객체
첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)
각 학생의 총점과 평균 계산
"""

scores = [(90, 80), (85, 75), (90, 100)]

for score in range(len(scores)):
    sum_score = 0
    for s in scores[score]:
        sum_score += s
    print(f'{score + 1}번 학생의 총점은 {sum_score}점이고, 평균은 {sum_score / 2}입니다.')