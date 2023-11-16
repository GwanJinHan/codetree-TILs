import sys
input = sys.stdin.readline

n = int(input())

matrix = [
    list(map(int, input().split())) for _ in range(n)
]

for i in range(n):
    for r in range(n):
        for c in range(n):
            if matrix[r][i] == 1 and matrix[i][c] == 1:
                matrix[r][c] = 1
            if r == c:
                matrix[r][c] = 1


for m in matrix:
    print(*m)