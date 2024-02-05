# 1과 2의 합으로 나타내기

n = int(input())

memo = [-1] * n

def square(num):
    if num == n:
        return 1
    elif num > n:
        return 0
    
    t1 = memo[num + 1] if num + 1 < n and memo[num + 1] != -1 else square(num + 1) 
    t2 = memo[num + 2] if num + 2 < n and memo[num + 2] != -1 else square(num + 2) 
    t = t1 + t2
    memo[num] = t

    return t

print(square(0) % 10007)