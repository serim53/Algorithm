# 최대한 많은 강의를 배정
import heapq
import sys

n = int(sys.stdin.readline())
result = 0
time = 0
arr = []
for _ in range(n):
    s, f = map(int, sys.stdin.readline().split())
    heapq.heappush(arr, [s, f])
while arr:
    s, f = heapq.heappop(arr)
    if s >= time:
        result += 1
        time = f
print(result)
