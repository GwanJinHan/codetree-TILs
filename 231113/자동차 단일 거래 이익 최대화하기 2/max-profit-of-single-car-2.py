# 구간 다시 시작하기
n = int(input())
arr = list(map(int, input().split( )))

min_val = arr[0]
ans = 0
for val in arr:
    if min_val > val:
        min_val = val
    elif min_val <= val:
        ans = max(ans, val - min_val) 

print(ans)