import sys
input = sys.stdin.readline

s = str(input().rstrip())
s_list = list(s)

N = int(input())
dp = [0] * (len(s_list) + 1)
dp[0] = 1

words = []
for _ in range(N):
    word = str(input().rstrip())
    words.append(word)

for i in range(len(s_list) + 1):
    for word in words:
        len_word = len(word)
        if i >= len_word and dp[i - len_word] == 1 and s_list[i - len_word:i] == list(word):
            dp[i] = 1

if dp[len(s_list)]:
    print(1)
else:
    print(0)