n = int(input())

a = b = 1

for i in range(n - 2):
    a, b = b, a + b

print(b)