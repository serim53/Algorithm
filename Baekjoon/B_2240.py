t, w = map(int, input().split())
info = [0] + [int(input()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t + 1)]
for i in range(t + 1):
    # 1번 자두나무에 계속 위치할 경우
    if info[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]
    # 이동할 경우
    for j in range(1, w + 1):
        if (info[i] == 2 and j % 2 == 1) or (info[i] == 1 and j % 2 == 0):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[t]))