import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = sys.maxsize

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

s, e = map(int, input().split())
d = [INF] * n
d[s - 1] = 0
path = [0] * n

hq = [(0, s - 1)]

while hq:
    w, i = heappop(hq)

    if d[i] != w:
        continue
    
    for node, weight in graph[i]:
        if d[node] > weight + d[i]:
            d[node] = weight + d[i]
            heappush(hq, (d[node], node))
            path[node] = i

print(d[e - 1])

x = e
ans = [x]

while x != s:
    x = path[x - 1] + 1
    ans.append(x)   

print(*ans[::-1])