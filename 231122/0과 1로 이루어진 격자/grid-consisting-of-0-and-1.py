import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int, list(input().rstrip()))) for _ in range(n)
]
ans = 0
for r in range(n - 1, -1, -1):
    for c in range(n - 1, -1, -1):
        if arr[r][c] == 1:
            ans += 1
            for i in range(r, -1, -1):
                for j in range(c, -1, -1):
                    arr[i][j] = 1 if arr[i][j] == 0 else 0

print(ans)