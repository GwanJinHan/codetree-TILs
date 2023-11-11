import sys
from functools import cmp_to_key
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

def compare(x, y):
    if x[0] > y[0]:
        return -1
    elif x[0] < y[0]:
        return 1
    else:
        if int(x + y) > int(y + x):
            return -1
        else:
            return 1

arr.sort(key = cmp_to_key(compare))

print("".join(arr))