"""
리스트 내포 기능을 이용하여 다음 문장으로부터 모음('aeiou')을 제거하시오
Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.
"""

word = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

for i in range(len(word)):
    if word[i] != 'a' and word[i] != 'e' and word[i] != 'i' and word[i] != 'o' and word[i] != 'u':
        print(word[i], end = "")