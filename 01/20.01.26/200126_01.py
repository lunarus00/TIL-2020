"""
이름과 나이를 입력받아
올해를 기준으로 100세가 되는 해를 표시
"""

name = input()
age = int(input())

import datetime

today = datetime.date.today()

year = today.year

for i in range(100):
    age += 1
    year += 1
    if age == 100:
        break

print('{0}(은)는 {1}년에 100세가 될 것입니다.'.format(name, year))