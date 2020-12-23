"""
콤마(,)로 구분된 정수를 입력받아 리스트와 튜플 객체를 생성
"""

word = input()

list_word = word.split(', ')

for i in range(len(list_word)):
    list_word[i] = int(list_word[i])

tuple_word = tuple(list_word)

print(list_word)
print(tuple_word)
