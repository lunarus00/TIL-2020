password = {
    '001101': '0',
    '010011': '1',
    '111011': '2',
    '110001': '3',
    '100011': '4',
    '110111': '5',
    '001011': '6',
    '111101': '7',
    '011001': '8',
    '101111': '9'
}

# number = '0DEC'
number = '0269FAC9A0'

pw_num = ''

for i in range(len(number)):
    b_num = bin(int(number[i], 16))
    b_num = b_num[2:6]
    while len(pw_num) + len(b_num) < (i+1) * 4:
        pw_num += '0'
    pw_num += b_num

i = 0
print(pw_num)
while i < len(pw_num):
    word = pw_num[i:i+6]
    if word in password.keys():
        print(password[word], end = ' ')
        i += 6
    else:
        i += 1
print()