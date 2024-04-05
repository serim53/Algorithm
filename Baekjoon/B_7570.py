import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
result = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    result[nums[i]] = i
cnt = 1
max_cnt = -1
for i in range(1, n):
    if result[i] < result[i + 1]:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1
print(n - max_cnt if max_cnt != - 1 else 0)