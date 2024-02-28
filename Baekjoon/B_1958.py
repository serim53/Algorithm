l = [input() for _ in range(3)]
l.sort(key=len)
w1, w2, w3 = l
l1, l2, l3 = len(w1), len(w2), len(w3)

dp = [[[0] * (l1 + 1) for _ in range(l2 + 1)] for _ in range(l3 + 1)]

for k in range(1, l3 + 1):
    for j in range(1, l2 + 1):
        for i in range(1, l1 + 1):
            if w1[i - 1] == w2[j - 1] == w3[k - 1]:
                dp[k][j][i] = dp[k - 1][j - 1][i - 1] + 1
            else:
                dp[k][j][i] = max(dp[k - 1][j][i], dp[k][j - 1][i], dp[k][j][i - 1])

print(dp[-1][-1][-1])