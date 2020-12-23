import sys
sys.stdin = open('find_matrix.txt')

def find_matrix(i, j):
    row_count = 0
    line_count = 0
    for k in range(i, N):
        if matrix[k][j] != 0:
            row = k
            row_count += 1
        else:
            break
    for k in range(j, N):
        if matrix[i][k] != 0:
            line = k
            line_count += 1
        else:
            break
    for k in range(i, row+1):
        for l in range(j, line + 1):
            visited[k][l] = 1
    untided_list.append((row_count, line_count))

def sort_matrix():
    i = 0
    while len(untided_list) > 0:
        min_mat = 999999
        long = len(untided_list)
        for j in range(long):
            mul = untided_list[j][0] * untided_list[j][1]
            if mul < min_mat:
                min_mat = mul
                a, b = untided_list[j][0], untided_list[j][1]
                num_pop = j
            elif mul == min_mat:
                if untided_list[j][0] < a:
                    a, b = untided_list[j][0], untided_list[j][1]
                    num_pop = j
        result.append(a)
        result.append(b)
        untided_list.pop(num_pop)
        i += 1

T = int(input())

for tc in range(T):
    N = int(input())
    matrix = []

    for i in range(N):
        matrix.append(list(map(int, input().split())))

    visited = [[0] * N for i in range(N)]

    untided_list = []
    result = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0 and visited[i][j] == 0:
                find_matrix(i, j)

    sort_matrix()

    print('#{} {}'.format(tc+1, int(len(result) / 2)), end = ' ')

    for i in range(len(result)):
        print(result[i], end = ' ')
    print()