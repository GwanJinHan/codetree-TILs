import sys
input = sys.stdin.readline

n = int(input())
nums = [input().rstrip() for _ in range(n)]
nums.sort(key=lambda x : x*5, reverse=True)
print(int("".join(nums)))