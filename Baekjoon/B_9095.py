T = int(input())

testList = []

for _ in range(T):
    testList.append(int(input()))

dp = [1, 2, 4]

for i in range(3, max(testList) + 1):
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

for num in testList:
    print(dp[num - 1])