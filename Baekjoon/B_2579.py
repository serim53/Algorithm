n = int(input())
array = [0] * 300
for i in range(n):
    array[i] = int(input())

dp = [0] * 300

dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[1] + array[2], dp[0] + array[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + array[i], dp[i - 3] + array[i - 1] + array[i])

print(dp[n - 1])