import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = sys.maxsize
matrix = [[INF] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a - 1][b - 1] = c

for i in range(n):
    for r in range(n):
        for c in range(n):
            matrix[r][c] = min(matrix[r][c], matrix[r][i] + matrix[i][c])

ans = sys.maxsize
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = min(ans, matrix[i][j] + matrix[j][i])

print(ans)