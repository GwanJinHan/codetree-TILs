import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
cnts = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    cnts[b - 1] += 1
    graph[a - 1].append(b - 1)

queue = deque([i for i in range(n) if cnts[i] == 0])
ans = []
while queue:
    cur = queue.popleft()
    ans.append(cur + 1)
    for i in graph[cur]:
        cnts[i] -= 1
        
        if cnts[i] == 0:
            queue.append(i)

print("Consistent" if sum(cnts) == 0 else "Inconsistent")