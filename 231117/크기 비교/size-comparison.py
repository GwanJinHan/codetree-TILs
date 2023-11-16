import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = -1

for i in range(n):
    for r in range(n):
        for c in range(n):
            if matrix[r][i] == 1 and matrix[i][c] == 1:
                matrix[r][c] = 1
            elif matrix[r][i] == -1 and matrix[i][c] == -1:
                matrix[r][c] = -1

for m in matrix:
    cnt = 0
    for val in m:
        if val == 0:
            cnt += 1
    print(cnt - 1)