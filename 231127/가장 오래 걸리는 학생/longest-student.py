import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = sys.maxsize

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

d = [INF] * n
d[n - 1] = 0
hq = [(0, n - 1)]

while hq:
    w, i = heappop(hq)

    if d[i] != w:
        continue

    for node, weight in graph[i]:
        if d[node] > d[i] + weight:
            d[node] = d[i] + weight
            heappush(hq, (d[node], node))

print(max(d))