n = int(input())
arr = list(map(int, input().split()))
max_dp, min_dp = arr, arr
# 메모리가 작으므로 계속해서 갱신을 시켜주는 방식으로 구현
for _ in range(n - 1):
    arr = list(map(int, input().split()))
    max_dp = [arr[0] + max(max_dp[0], max_dp[1]), arr[1] + max(max_dp), arr[2] + max(max_dp[1], max_dp[2])]
    min_dp = [arr[0] + min(min_dp[0], min_dp[1]), arr[1] + min(min_dp), arr[2] + min(min_dp[1], min_dp[2])]
print(max(max_dp), min(min_dp))