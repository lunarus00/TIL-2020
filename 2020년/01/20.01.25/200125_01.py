"""
5명의 학생의 점수에 대해 60점 이상일 때 합격 메시지 출력,
60점 미만일 때 불합격 메시지를 출력하라

ex) 1번 학생은 88점으로 합격입니다.

"""

point = [88, 30, 61, 55, 95]

for i in range(len(point)):
    if point[i] >= 60:
        print(f'{i+1}번 학생은 {point[i]}점으로 합격입니다.')
    else:
        print(f'{i+1}번 학생은 {point[i]}점으로 불합격입니다.')