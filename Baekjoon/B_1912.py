n = int(input())
array = list(map(int, input().split()))
dp = [array[0]]
for i in range(len(array) - 1):
    dp.append(max(dp[i] + array[i + 1], array[i + 1]))
print(max(dp))