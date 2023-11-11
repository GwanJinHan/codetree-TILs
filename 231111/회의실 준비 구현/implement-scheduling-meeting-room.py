import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

arr.sort(key = lambda x : x[1])

prev = 0
cnt = 0
for start, end in arr:
    if prev <= start:
        cnt += 1
        prev = end

print(cnt)