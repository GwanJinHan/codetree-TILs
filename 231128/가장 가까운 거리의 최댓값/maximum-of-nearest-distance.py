import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = sys.maxsize

a, b, c = map(int, input().split())

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s - 1].append((e - 1, w))
    graph[e - 1].append((s - 1, w))

arrs = []
for start in [a, b, c]:
    d = [INF] * n
    d[start - 1] = 0

    hq = [(0, start - 1)]

    while hq:
        w, i = heappop(hq)

        if d[i] < w:
            continue
        
        for node, weight in graph[i]:
            if d[node] > weight + d[i]:
                d[node] = weight + d[i]
                heappush(hq, (d[node], node))

    arrs.append(d)

ans = -1
for i in range(n):
    # if i == a - 1 or i == b - 1 or i == c - 1:
    #     continue
    acc = INF
    for arr in arrs:
        acc = min(acc, arr[i])
    
    ans = max(ans, acc)

print(ans)