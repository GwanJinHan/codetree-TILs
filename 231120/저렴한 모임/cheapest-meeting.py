# 만날 곳 - 도착할 곳 => 만날 곳 정하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
v1, v2, e = map(int, input().split())
INF = sys.maxsize
matrix = [[INF] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a - 1][b - 1] = c
    matrix[b - 1][a - 1] = c

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if r == c or inter == r or inter == c:
                continue
            
            if matrix[r][c] > matrix[r][inter] + matrix[inter][c]:
                matrix[r][c] = matrix[r][inter] + matrix[inter][c]
            
ans = INF

for i in range(n): #만날 곳
    ans = min(ans, matrix[v1 - 1][i] + matrix[v2 - 1][i] + matrix[i][e - 1])

print(ans if ans != INF else -1)