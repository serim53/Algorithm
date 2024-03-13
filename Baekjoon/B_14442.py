from collections import deque

def bfs():
    q = deque()
    q.append([0, 0, k])
    visited[0][0][k] = 1
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z > 0 and visited[nx][ny][z - 1] == 0:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    q.append([nx, ny, z - 1])
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])
    return -1

n, m, k = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
print(bfs())