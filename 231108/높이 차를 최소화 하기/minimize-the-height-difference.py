# BFS + 이진탐색

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]


left, right = 0, 500

answer = sys.maxsize

while left <= right:
    mid = (left + right) // 2

    queue = deque([(0, 0, arr[0][0], arr[0][0])])
    visit = [[sys.maxsize] * m for _ in range(n)]
    ans = 0
    while queue:
        r, c, M, N = queue.popleft()


        if visit[r][c] <= M - N:
            continue
        ans = max(ans, M - N) 
        
        visit[r][c] = M - N

        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]

            if 0 <= nr < n and 0 <= nc < m and M - N < visit[nr][nc]:
                if max(M, arr[nr][nc]) - min(N, arr[nr][nc]) <= mid:
                    queue.append((nr, nc, max(M, arr[nr][nc]), min(N, arr[nr][nc])))

    if visit[n - 1][m - 1] != sys.maxsize:
        right = mid - 1
        answer = min(answer, ans)
    else:
        left = mid + 1

print(answer)