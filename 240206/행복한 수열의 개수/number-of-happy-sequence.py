import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [
    list(map(int, input().split())) for _ in range(n)
]
ans = 0

for r in range(n):
    cnt = 1
    pre = 0
    for c in range(n):
        if pre == matrix[r][c]:
            cnt += 1
        if cnt == m:
            ans += 1
            break            
        pre = matrix[r][c]

for c in range(n):
    cnt = 1
    pre = 0
    for r in range(n):
        if pre == matrix[r][c]:
            cnt += 1
        if cnt == m:
            ans += 1
            break
        pre = matrix[r][c]

print(ans)