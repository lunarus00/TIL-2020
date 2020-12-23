import sys
sys.stdin = open('binary.txt')

T = int(input())

def bin_num(number):
    global bin_word
    if len(bin_word) >= 13:
        bin_word = 'overflow'
        return
    elif number == 1:
        bin_word += '1'
        return
    elif int(number) == 1:
        number -= 1
        bin_word += '1'
    else:
        bin_word += '0'
    bin_num(number*2)

for tc in range(T):
    number = float(input())
    bin_word = ''
    bin_num(number*2)
    print('#{} {}'.format(tc+1, bin_word))