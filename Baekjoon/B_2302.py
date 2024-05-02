n = int(input().rstrip())
m = int(input().rstrip())
vip = [int(input().rstrip()) for _ in range(m)]
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
result = 1
if m > 0:
    temp = 0
    for j in range(m):
        result *= dp[vip[j] - 1 - temp]
        temp = vip[j]
    result *= dp[n - temp]
else:
    result = dp[n]
print(result)