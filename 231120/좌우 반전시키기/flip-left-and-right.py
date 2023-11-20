# 첫 번째 위치 누르기 불가
# 왼, 누, 오 반전
# 모두 1

n = int(input())
arr = list(map(int, input().split()))

# 00 -> 오른쪽 0 누르기
# 01 -> 오른쪽 1 누르기
def switch(num):
    return 0 if num == 1 else 1

ans = 0
flag = False
for i in range(n):
    if arr[i] == 0:
        if flag: # 00
            arr[i - 1] = 1
            arr[i] = 1
            if i + 1 < n:
                arr[i + 1] = switch(arr[i + 1])
            ans += 1
            flag = False
        else:
            flag = True
    else:
        if flag: # 01
            arr[i - 1] = 1
            arr[i] = 0
            if i + 1 < n:
                arr[i + 1] = switch(arr[i + 1])
            ans += 1
    
print(ans if all(arr) else -1)