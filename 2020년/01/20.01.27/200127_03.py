"""
구구단 2단부터 9단까지
3의 배수거나 7의 배수인 수를 제외한 값을 리스트 객체 result 안에
각 단마다 리스트를 만들어 삽입하고 이를 출력
"""

result = []

for i in range(2, 10):
    re_ij = []
    for j in range(1, 10):
        if (i * j) % 3 != 0 and (i * j) % 7 != 0:
            re_ij.append(i * j)
    result.append(re_ij)

print(result)