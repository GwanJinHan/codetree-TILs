from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
INF = sys.maxsize

arr = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a - 1].append((b - 1, c))
    arr[b - 1].append((a - 1, c))

queue = [(0, k - 1)]
d = [INF] * n
d[k - 1] = 0

while queue:
    w, i = heappop(queue)

    if d[i] != w:
        continue
    
    for node, weight in arr[i]:
        if d[i] + weight < d[node]:
            d[node] = d[i] + weight
            heappush(queue, (d[node], node))


for val in d:
    print(val if val != INF else -1)