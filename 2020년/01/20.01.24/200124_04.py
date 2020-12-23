"""
두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 게임
["가위", "바위", "보"] 리스트를 활용
"""
gb = ["가위", "바위", "보"]

Man1 = input()
Man2 = input()

for i in range(len(gb)):
    if Man1 == gb[i]:
        man1 = i
    if Man2 == gb[i]:
        man2 = i

if man1 > man2:
    if man1 == 2:
        if man2 == 0:
            print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
if man1 == man2:
    print('Result : Draw')
if man2 > man1:
    if man2 == 2:
        if man1 == 0:
            print('Result : Man1 Win!')
    else:
        print('Result : Man2 Win!')
