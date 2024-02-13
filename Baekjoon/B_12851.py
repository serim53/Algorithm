import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
queue = deque([n])
cnt = 0
result = 0
visited = [0] * 100001

while queue:
    now = queue.popleft()
    if now == k:
        result = visited[now]
        cnt += 1
        continue
    for next in (now - 1, now + 1, now * 2):
        if 0 <= next <= 100000 and (not visited[next] or visited[next] == visited[now] + 1):
            visited[next] = visited[now] + 1
            queue.append(next)

print(result)
print(cnt)