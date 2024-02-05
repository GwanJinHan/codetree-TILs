import sys
input = sys.stdin.readline

n = int(input())
matrix = [
    list(map(int, input().split())) for _ in range(n)
]
ans = 0
for r in range(n - 2):
    for c in range(n - 2):
        t = 0
        for i in range(3):
            for j in range(3):
                t += matrix[r + i][c + j]
        ans = max(ans, t)

print(ans)