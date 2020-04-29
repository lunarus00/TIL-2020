data = '0000000111100000011000000111100110000110000111100111100111111001100111'

data_list = []

for i in range(0, len(data), 7):
    data_list.append(data[i:i+7])

for i in range(len(data_list)):
    print(int(data_list[i], 2))