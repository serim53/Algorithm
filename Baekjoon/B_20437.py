from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = input()
    k = int(input())
    dic = defaultdict(list)
    min_len = 1e9
    max_len = -1
    for i in range(len(word)):
        dic[word[i]].append(i)
    for key in dic.keys():
        arr = dic[key]
        if len(arr) >= k:
            for i in range(len(arr) - k + 1):
                length = arr[i + k - 1] - arr[i]
                min_len = min(min_len, length)
                max_len = max(max_len, length)
    if min_len == 1e9:
        print(-1)
    else:
        print(min_len + 1, max_len + 1)