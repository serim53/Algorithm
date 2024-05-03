number = list(map(int, input().rstrip()))
l = len(number)
dp = [0] * (l + 1)
dp[0] = 1
dp[1] = 1
if number[0] == 0:
    print(0)
else:
    for i in range(1, l):
        j = i + 1
        if number[i] > 0:
            dp[j] += dp[j - 1]
        if 10 <= 10 * number[i - 1] + number[i] <= 26:
            dp[j] += dp[j - 2]
    print(dp[-1] % 1000000)