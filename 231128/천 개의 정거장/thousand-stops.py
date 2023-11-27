# 최소 비용 중 -> 최소 시간 (최소 비용이 우선) 
from collections import defaultdict as dd
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


a, b, n = map(int, input().split())
# graph = [[] for _ in range(1000)]
graph = dd(dict)
INF = sys.maxsize

for _ in range(n):
    fee, cnt = map(int, input().split())
    path = list(map(int, input().split()))

    for i in range(cnt - 1): # 출발점
        for j in range(i + 1, cnt):
            try:
                if graph[path[i] - 1][path[j] - 1][1] > fee:
                    graph[path[i] - 1][path[j] - 1] = (path[j] - 1, fee, j - i)
            except:
                graph[path[i] - 1][path[j] - 1] = (path[j] - 1, fee, j - i)

d = [INF] * 1000
time = [INF] * 1000
d[a - 1] = 0
hq = [(0, 0, a - 1)]

while hq:
    w, t, i = heappop(hq)

    if d[i] < w:
        continue
    
    for node, fee, tt in graph[i].values():
        if d[node] > fee + d[i]:
            d[node] = fee + d[i]
            time[node] = min(t + tt, time[i] + tt)
            heappush(hq, (d[node], time[node], node))
        elif d[node] == fee + d[i]:
            time[node] = min(time[node], t + tt, time[i] + tt)

if d[b - 1] >= INF:
    print(-1, -1)
else:
    print(d[b - 1], time[b - 1])