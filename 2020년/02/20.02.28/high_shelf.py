import sys
sys.stdin = open('high_shelf.txt')

T = int(input())

def find_tower():
    global result
    for i in range(1<<N):
        sum_check = 0
        for j in range(N):
            if i & (1<<j):
                sum_check += members[j]
            if sum_check >= B:
                a = sum_check - B
                if a < result:
                    result = a
                break

for tc in range(T):
    N, B = list(map(int, input().split()))
    members = list(map(int, input().split()))

    result = 9999999

    find_tower()
    print('#{} {}'.format(tc+1, result))