n = int(input())

memo = [-1] * n

def square(num):
    if n == num:
        return 1
    elif n < num:
        return 0

    t1 = memo[num + 1] if num + 1 < n and memo[num + 1] != -1 else square(num + 1)
    t2 = memo[num + 2] if num + 2 < n and memo[num + 2] != -1 else square(num + 2) * 2
    t = t1 + t2
    memo[num] = t
    return t

print(square(0) % 10007)