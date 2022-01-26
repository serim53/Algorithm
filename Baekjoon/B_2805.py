import sys

M, N = map(int, sys.stdin.readline().split())
len = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(len)

while start <= end:
    mid = (start + end) // 2
    get = 0
    for i in len:
        if i >= mid:
            get += i - mid
    if get >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
