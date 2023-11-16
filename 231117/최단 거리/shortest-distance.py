import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [
    list(map(int, input().split())) for _ in range(n)
]

for i in range(n):
    for r in range(n):
        for c in range(n):
            matrix[r][c] = min(matrix[r][c], matrix[r][i] + matrix[i][c])

for _ in range(m):
    a, b = map(int, input().split())
    print(matrix[a - 1][b - 1])