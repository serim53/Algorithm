n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
nums = []
max_len = max(dp)
for i in range(n - 1, -1, -1):
    if dp[i] == max_len:
        nums.append(arr[i])
        max_len -= 1
nums.reverse()
print(*nums)