# 최대한 큰 점수를 내는 법 : 크게 지고 작게 이긴다
import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()

ans = 0
prev = 1
for i in range(1, n):
    if arr[i - 1] + 1 != arr[i] :
        if arr[i] - arr[i - 1] - 1 > prev:
            ans += prev
        else:
            ans += arr[i] - arr[i - 1] - 1 
        prev = 1
    else:
        prev += 1

print(ans)