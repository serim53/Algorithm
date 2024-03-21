import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = max(dp[i], dp[i - 1])
    day = i + info[i][0] - 1
    if day < n:
        dp[day] = max(dp[day], dp[i - 1] + info[i][1])
print(max(dp))