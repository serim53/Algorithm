n, k = map(int, input().split())
products = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
for p in products:
    w, v = p
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])