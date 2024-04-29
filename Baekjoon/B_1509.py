input_str = input()
l = len(input_str)
dp = [2500 for _ in range(l + 1)]
dp[-1] = 0
is_p = [[0 for _ in range(l)] for _ in range(l)]

for i in range(l):
    is_p[i][i] = 1

for i in range(1, l):
    if input_str[i - 1] == input_str[i]:
        is_p[i - 1][i] = 1

for idx in range(3, l + 1):
    for start in range(l - idx + 1):
        end = start + idx - 1
        if input_str[start] == input_str[end] and is_p[start + 1][end - 1]:
            is_p[start][end] = 1

for end in range(l):
    for start in range(end + 1):
        if is_p[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[l - 1])