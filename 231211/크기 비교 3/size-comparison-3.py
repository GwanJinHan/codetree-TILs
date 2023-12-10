import sys
from heapq import *
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
cnts = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    cnts[b - 1] += 1
    graph[a - 1].append(b - 1)

queue = [i for i in range(n) if cnts[i] == 0]
ans = []
while queue:
    cur = heappop(queue)
    ans.append(cur + 1)
    for i in graph[cur]:
        cnts[i] -= 1
        
        if cnts[i] == 0:
            heappush(queue, i)

print(*ans)