"""
1~10까지의 정수를 항목으로 갖는 리스트
filter 함수와 람다식으로 짝수만을 선택해 리스트 반환
"""

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, num_list))

print(result)