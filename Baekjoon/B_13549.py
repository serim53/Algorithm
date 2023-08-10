from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while queue:
    now = queue.popleft()
    if now == k:
        print(visited[now])
        break
    if 0 <= now - 1 < 100001 and visited[now - 1] == -1:
        visited[now - 1] = visited[now] + 1
        queue.append(now - 1)
    if 0 <= now * 2 < 100001 and visited[now * 2] == -1:
        visited[now * 2] = visited[now]
        queue.appendleft(now * 2)
    if 0 <= now + 1 < 100001 and visited[now + 1] == -1:
        visited[now + 1] = visited[now] + 1
        queue.append(now + 1)