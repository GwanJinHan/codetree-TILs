import sys
input = sys.stdin.readline
sys.set_int_max_str_digits(0)

n = int(input())
nums = [input().rstrip() for _ in range(n)]
nums.sort(key=lambda x : x*5, reverse=True)
print(int("".join(nums)))