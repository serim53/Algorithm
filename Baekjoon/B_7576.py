from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0] * m for _ in range(n)]
queue = deque()
flag = 1
max_val = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
            visited[i][j] = 1
if len(queue) == m * n:
    flag = 0
if flag:
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1
    for i in range(n):
        max_val = max(max_val, max(graph[i]))
        if 0 in graph[i]:
            flag = -1
            break
if flag > 0:
    print(max_val - 1)
else:
    print(flag)