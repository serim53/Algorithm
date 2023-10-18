from collections import deque


n = int(input())
visited = [0] * (n + 1)
parent = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited[1] = 1
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if not visited[i]:
            parent[i] = now
            queue.append(i)
            visited[i] = 1

for i in range(2, n + 1):
    print(parent[i])