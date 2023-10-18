# 홀수번째
# fn = f(n // 2 + 1) ** 2 + f(n // 2) ** 2
# 짝수번째
# fn = f(n // 2 + 1) ** 2 - f(n // 2 - 1) ** 2

dp = {}


def fibo(n):
    if dp.get(n):
        return dp[n]
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n % 2 == 0:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007
        dp[n // 2 - 1] = fibo(n // 2 - 1) % 1000000007
        return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
    else:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007
        dp[n // 2] = fibo(n // 2) % 1000000007
        return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2


n = int(input())
print(fibo(n) % 1000000007)