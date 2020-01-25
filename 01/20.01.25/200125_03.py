"""
학생의 점수를 나타내는 리스트
[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while 문과 리스트 객체의 pop()를 이용해 80점 이상의 점수의 총합 구하기

ex) 454

"""

score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

sum_score = 0
i = 0

while i<10:
    pop_score = score.pop()
    if pop_score >= 80:
        sum_score += pop_score
    i += 1

print(sum_score)