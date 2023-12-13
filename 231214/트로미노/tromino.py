import sys
input=sys.stdin.readline

n, m = map(int, input().split())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

answer = 0
for r in range(n):
    for c in range(m):
        if 0 < c < m - 1:
            answer = max(answer, sum([arr[r][c - 1], arr[r][c], arr[r][c + 1]]))
        if 0 < r < n - 1:
            answer = max(answer, sum([arr[r - 1][c], arr[r][c], arr[r + 1][c]]))

        if 0 < r < n and 0 <= c < m - 1:
            answer = max(answer, sum([arr[r - 1][c], arr[r][c], arr[r][c + 1]]))
        if 0 <= r < n - 1 and 0 <= c < m - 1:
            answer = max(answer, sum([arr[r][c], arr[r][c + 1], arr[r + 1][c]]))
        if 0 < r < n and 0 < c < m:
            answer = max(answer, sum([arr[r][c], arr[r - 1][c], arr[r][c - 1]]))
        if 0<= r < n - 1 and 0 < c < m:
            answer = max(answer, sum([arr[r][c], arr[r + 1][c], arr[r][c - 1]]))

print(answer)