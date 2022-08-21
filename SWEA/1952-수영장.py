test_case = int(input())
for tc in range(1, test_case + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] + plan
    months, year = 1e9, 1e9
    for i in range(1, 13):
        day = dp[i] * price[0] + dp[i - 1]
        month = price[1] + dp[i - 1]
        if i >= 3:
            months = price[2] + dp[i - 3]
        if i >= 12:
            year = price[3] + dp[i - 12]
        dp[i] = min(day, month, months, year)
    print("#{} {}".format(tc, dp[-1]))
