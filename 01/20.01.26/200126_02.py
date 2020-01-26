"""
ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC
문자열
A는 4점, B는 3점, C는 2점, D는 1점
알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하시오.
"""

word = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

list_word = list(map(lambda x: x, word))

for i in range(len(list_word)):
    if list_word[i] == 'A':
        list_word[i] = 4
    elif list_word[i] == 'B':
        list_word[i] = 3
    elif list_word[i] == 'C':
        list_word[i] = 2
    elif list_word[i] == 'D':
        list_word[i] = 1

sum_word = 0

for i in range(len(list_word)):
    sum_word += list_word[i]

print(sum_word)