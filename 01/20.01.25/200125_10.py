"""
인자로 전달된 두 개의 문자열 중 길이가 더 긴 것을 출력
"""

def long_check(word):
    if len(word[0]) > len(word[1]):
        print(word[0])
    else:
        print(word[1])

words = input()
word = words.split(', ')

long_check(word)