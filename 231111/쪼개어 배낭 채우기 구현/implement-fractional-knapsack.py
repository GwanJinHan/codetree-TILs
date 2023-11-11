import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v, v / w))

arr.sort(key = lambda x : -x[2])


cur_bag = 0
ans = 0
for w, v, _ in arr:
    cur_bag += w
    if cur_bag > m:
        ans += v * (m - cur_bag + w) / w
        break
    ans += v

print("%.3f" %round(ans, 3))