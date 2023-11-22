import sys
input = sys.stdin.readline

INF = sys.maxsize
n, m, p, q = map(int, input().split())
matrix = [[INF] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a - 1][b - 1] = c

for inter in range(n):
    for r in range(n):
        for c in range(n):
            if matrix[r][c] > matrix[r][inter] + matrix[inter][c]:
                matrix[r][c] = matrix[r][inter] + matrix[inter][c]

cnt = 0
acc = 0
for _ in range(q):
    a, b = map(int, input().split())

    tmp = INF
    for i in range(p):
        tmp = min(tmp, matrix[a - 1][i] + matrix[i][b - 1])
    
    if tmp < INF:
        cnt += 1
        acc += tmp

print(cnt)
print(acc)