import sys
from heapq import heappush, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = sys.maxsize

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b - 1].append((a - 1, c))

hq = [(0, n - 1)]
d = [INF] * n
d[n - 1] = 0

while hq:
    w, i = heappop(hq)

    if d[i] != w:
        continue

    for node, weight in graph[i]:
        if d[node] > weight + d[i]:
            d[node] = weight + d[i]
            heappush(hq, (d[node], node))

for i in range(n):
    if d[i] == INF:
        d[i] = -1

print(max(d))