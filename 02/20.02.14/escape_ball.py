import sys
sys.stdin = open('escape_ball.txt')

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    field = []
    for i in range(N):
        field.append(list(map(lambda x: x, input().split())))
    