import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)] + [2 * n + 1]
arr.sort()

ans = 0
prev = 1

for i in range(1, n + 1):
    if arr[i - 1] + 1 != arr[i] :
        if arr[i] - arr[i - 1] - 1 > prev:
            ans += prev
            prev = 1
        else:
            ans += arr[i] - arr[i - 1] - 1 
            prev -= arr[i] - arr[i - 1] - 2
    else:
        prev += 1

print(ans)