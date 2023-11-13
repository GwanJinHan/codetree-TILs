# 다음에 조금이라도 떨어지면 판다. (혹은 판 상태를 유지한다.)
# 다음에 조금이라도 오르면 산다. (혹은 산 상태를 유지한다.)

import sys

n = int(input())
arr = list(map(int, input().split( ))) + [0]

ans = 0
buy_price = sys.maxsize

for i in range(1, n + 1):
    if arr[i] > arr[i - 1]:
        buy_price = min(buy_price, arr[i - 1])
    elif arr[i] < arr[i - 1]:
        ans = max(ans, arr[i - 1] - buy_price)
        buy_price = sys.maxsize

print(ans)