n = int(input())
arr = list(map(int, input().split()))

acc = 0
ans = 0
for val in arr:
    acc += val
    ans = max(acc, ans)
    if acc < 0 :
        acc = 0

print(ans)