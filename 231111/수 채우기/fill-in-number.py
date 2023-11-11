n = int(input())

cnt = n // 5
cur = n % 5

while cur != 0 and cnt >= 0:
    if cur % 2 == 0:
        cnt += cur // 2
        break
    else:
        cur += 5
        cnt -= 1

print(cnt)