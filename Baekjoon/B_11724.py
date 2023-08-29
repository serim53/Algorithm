from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = 1
                queue.append(node)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            result += 1
            visited[i] = 1
        else:
            bfs(i)
            result += 1

print(result)