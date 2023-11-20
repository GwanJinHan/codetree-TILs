n = int(input())
a = list(input())
b = list(input())

ans = 0

def switch(end):
    for i in range(end + 1):
        a[i] = 'G' if a[i] == 'H' else 'H'

for i in range(n - 1, -1, -1):
    if a[i] != b[i]:
        ans += 1
        switch(i)

print(ans)