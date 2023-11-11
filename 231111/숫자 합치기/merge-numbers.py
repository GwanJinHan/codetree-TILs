from heapq import heappush, heappop, heapify

n = int(input())
arr = list(map(int, input().split()))
heapify(arr)
ans = 0
while len(arr) != 1:
    a = heappop(arr)
    b = heappop(arr)

    heappush(arr, a + b)
    ans += (a + b)

print(ans)