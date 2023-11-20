n = int(input())
a = input() #초기 문자열
b = input() #목표 문자열

ans = 0
flag = 0
for i in range(n):
    if a[i] == b[i]:
        if flag:
            ans += 1
            flag = False
    else:
        flag = True

print(ans)