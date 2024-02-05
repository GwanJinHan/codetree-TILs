n = int(input())

memo = [-1] * n

def stair(num):
    if num == n - 1 or num > n:
        return 0
    if num == n:
        return 1

    t1 = memo[num + 2] if num + 2 < n and memo[num + 2] != -1 else stair(num + 2)
    t2 = memo[num + 3] if num + 3 < n and memo[num + 3] != -1 else stair(num + 3)
    t = t1 + t2
    memo[num] = t
    return t

print(stair(0) % 10007)