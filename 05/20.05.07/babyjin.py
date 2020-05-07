import sys
sys.stdin = open('babyjin.txt')

T = int(input())

def find_babyjin(find_list):
    global flag
    for j in range(len(find_list)):
        fir_num = find_list[j]
        for k in range(len(find_list)):
            if j != k:
                sec_num = find_list[k]
            else:
                continue
            if fir_num == sec_num or fir_num == sec_num + 1 or fir_num == sec_num - 1:
                for l in range(len(find_list)):
                    if l != j and l != k:
                        thi_num = find_list[l]
                        if fir_num == sec_num == thi_num:
                            flag = 1
                            return
                        else:
                            if fir_num == sec_num + 1:
                                if thi_num == fir_num + 1 or thi_num == sec_num - 1:
                                    flag = 1
                                    return
                            elif fir_num == sec_num - 1:
                                if thi_num == fir_num - 1 or thi_num == sec_num + 1:
                                    flag = 1
                                    return
            else:
                continue

for tc in range(T):
    card_list = list(map(int, input().split()))
    first_player = []
    second_player = []
    for i in range(12):
        flag = 0
        if i % 2 == 0 or i == 0 :
            first_player.append(card_list[i])
            if i >= 4:
                find_babyjin(first_player)
                if flag == 1:
                    print('#{} 1'.format(tc+1))
                    break
        else:
            second_player.append(card_list[i])
            if i >= 4:
                find_babyjin(second_player)
                if flag == 1:
                    print('#{} 2'.format(tc+1))
                    break
        if i == 11:
            print('#{} 0'.format(tc+1))