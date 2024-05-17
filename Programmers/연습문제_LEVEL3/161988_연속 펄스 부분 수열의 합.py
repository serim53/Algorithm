def solution(sequence):
    dp = [[0, 0] for _ in range(len(sequence))]
    dp[0] = [sequence[0], sequence[0]]

    for i in range(1, len(sequence)):
        num = sequence[i]
        if i % 2:
            num = -num
        dp[i][0] = min(num, num + dp[i - 1][0])
        dp[i][1] = max(num, num + dp[i - 1][1])

    return max(max(map(max, dp)), -min(map(min, dp)))