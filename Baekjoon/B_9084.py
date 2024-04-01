t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m + 1)
    dp[0] = 1
    for c in coins:
        for i in range(c, m + 1):
            dp[i] += dp[i - c]
    print(dp[m])