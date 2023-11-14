import sys
input = sys.stdin.readline

n = int(input())
dp = {}

for _ in range(n):
    score, time = map(int, input().split())

    try:
        dp[time] = max(dp[time], score)
    except:
        dp[time] = score

print(sum(dp.values()))