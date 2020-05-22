import sys, time

start = time.time()

sys.stdin = open('MST.txt')

T = int(input())

for tc in range(T):
    V, E = list(map(int, input().split()))
    line_list = []
    for i in range(E):
        line_list.append(list(map(int, input().split())))
    

print(time.time() - start)