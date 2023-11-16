import sys
input = sys.stdin.readline

n = int(input())

matrix = [
    list(map(int, input().split())) for _ in range(n)
]

for i in range(n):
    for r in range(n):
        for c in range(n):
            if matrix[r][i] and matrix[i][c]:
                matrix[r][c] = 1


for m in matrix:
    print(*m)