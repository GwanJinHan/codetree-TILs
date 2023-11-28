import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n)]
INF = sys.maxsize

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

dist = []
for start in range(n):
    d = [INF] * n
    d[start] = 0
    hq = [(0, start)]

    while hq:
        w, i = heappop(hq)

        if d[i] < w:
            continue

        for node, weight in graph[i]:
            if d[node] > d[i] + weight:
                d[node] = d[i] + weight
                heappush(hq, (d[node], node))
    
    dist.append(d)

ans = -1
for i in range(n):
    ans = max(ans, dist[i][x - 1] + dist[x - 1][i])

print(ans)