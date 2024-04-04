from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
q = deque()
for i in range(n):
    while q and q[-1][1] > a[i]:
        q.pop()
    q.append([i, a[i]])
    if q[0][0] <= i - l:
        q.popleft()
    print(q[0][1], end=' ')