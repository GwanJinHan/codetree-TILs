import sys
input = sys.stdin.readline

n = int(input())

arr = [
    list(map(int, input().split())) for _ in range(n)
]

# 기준이 중앙이 아닌 십자의 위쪽 
dx, dy = [0, -1, 1, 0], [1, 1, 1, 2] #중, 왼, 오, 아래

# 왼위에서부터 순차적으로
ans = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == 0:
            ans += 1
            arr[r][c] = 1
            for i in range(4):
                ny, nx = r + dy[i], c + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    arr[ny][nx] = 0 if arr[ny][nx] == 1 else 1

# 불가능한 경우 -> 그냥 탐색
for r in range(n):
    for c in range(n):
        if arr[r][c] == 0:
            print(-1)
            sys.exit(0)

print(ans)