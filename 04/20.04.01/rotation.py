import sys
sys.stdin = open('rotation.txt')

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    for i in range(M):
        number = num_list.pop(0)
        num_list.append(number)
    print("#{} {}".format(tc+1, num_list[0]))