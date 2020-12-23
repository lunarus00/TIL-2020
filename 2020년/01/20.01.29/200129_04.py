"""
단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력
"""

words = input()
spl_word = words.split(', ')
spl_word.sort()

pri_word = ''

for i in range(len(spl_word)):
    pri_word += spl_word[i]
    pri_word += ', '

print(pri_word[:-2])