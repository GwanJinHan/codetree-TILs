n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

cnt = 0
while k > 0:
    coin = arr.pop()
    cnt += k // coin
    k %= coin

print(cnt)