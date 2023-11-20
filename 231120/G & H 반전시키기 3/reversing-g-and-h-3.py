n = int(input())
a = input()
b = input()

ans = 0
flag = False

for i in range(n):
    if a[i] != b[i]:
        if flag:
            cnt += 1
            if cnt == 4:
                ans += 1
                flag = False
        else:
            flag = True
            cnt = 1
    else:
        if flag:
            ans += 1
            flag = False

print(ans)