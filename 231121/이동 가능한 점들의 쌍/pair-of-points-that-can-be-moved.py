import sys
input = sys.stdin.readline

INF = sys.maxsize
n, m, p, q = map(int, input().split())
matrix = [[INF] * n for _ in range(n)]
matrix_red = [[False] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a - 1][b - 1] = c

for i in range(p):
    for j in range(n):
        matrix_red[j][i] = True
        matrix_red[i][j] = True

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c or r == inter or c == inter:
                continue
            if matrix[r][c] > matrix[r][inter] + matrix[inter][c] and (matrix_red[r][inter] or matrix_red[inter][c]):
                matrix[r][c] = matrix[r][inter] + matrix[inter][c]
                matrix_red[r][c] = True

for _ in range(q):