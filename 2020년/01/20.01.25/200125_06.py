"""
반복문을 이용하여 단어의 순서를 거꾸로 해 반환하는 함수 작성
함수를 이용해 회문 여부를 판단하는 코드
"""

pal_word = ''

def check_pal(word):
    for i in range(len(word)):
        pal_word = word[::-1]
    return pal_word == word

word = input()
abc = check_pal(word)

if abc == True:
    print('입력하신 단어는 회문(Palindrome)입니다.')
else:
    print('입력하신 단어는 회문이 아닙니다.')