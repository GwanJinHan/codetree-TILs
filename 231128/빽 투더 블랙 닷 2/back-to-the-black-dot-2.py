import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
red_one, red_two = map(int, input().split())
graph = [[] for _ in range(n)]
INF = sys.maxsize

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

reds = []
for red in [red_one, red_two]:
    d = [INF] * n
    d[red - 1] = 0
    hq = [(0, red - 1)]

    while hq:
        w, i = heappop(hq)
        
        if d[i] < w:
            continue

        for node, weight in graph[i]:
            if d[node] > weight + d[i]:
                d[node] = weight + d[i]
                heappush(hq, (d[node], node))

    reds.append(d)
ans = INF
for i in range(n):
    if i == red_one - 1 or i == red_two - 1:
        continue
    ans = min(ans, reds[0][i] + reds[0][red_two - 1] + reds[1][i])

if ans >= INF:
    print(-1)
else:
    print(ans)