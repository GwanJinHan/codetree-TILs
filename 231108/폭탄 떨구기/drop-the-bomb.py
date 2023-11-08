import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

# x - r 을 첫 번째 점에 맞추고 -> 터짐 표시하고 -> 그 다음 남은 점을 x - r 에 맞추고...

def isPossible(r):
    cnt = 0
    pointer = prev = 0 # 폭탄 범위 중 가장 왼쪽 (인덱스 기준)

    while cnt < k:
        cnt += 1
        while pointer < n and arr[prev] <= arr[pointer] <= arr[prev] + r * 2 :
            pointer += 1
        
        prev = pointer
    
    return False if cnt == k and pointer < n else True

left, right = 0, 1000000000

ans = sys.maxsize
while left <= right:
    mid = (left + right) // 2

    if isPossible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)