from collections import deque

def bfs(x, y):
    graph[x][y] = 0
    area = 1
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0
                area += 1
    return area


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            result = max(bfs(i, j), result)

print(cnt)
print(result)