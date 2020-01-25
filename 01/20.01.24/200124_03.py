"""
입력된 영어 알파벳 문자에 대해 대소문자를 구분하라.
"""

word = input()

if (word.isupper()) == True:
    print(f'{word}는 대문자 입니다.')
elif (word.islower()) == True:
    print(f'{word}는 소문자 입니다.')
else:
    print('영어 알파벳을 입력하세요.')

# fail 오답이 되는 이유가 뭐지?