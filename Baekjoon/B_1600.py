from collections import deque

def bfs():
    q = deque()
    q.append([0, 0, k])
    visited[0][0][k] = 0
    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1:
            return visited[x][y][z]
        if z > 0:
            for hdir in range(8):
                nx, ny = x + hdx[hdir], y + hdy[hdir]
                if 0 <= nx < h and 0 <= ny < w:
                    if visited[nx][ny][z - 1] == -1 and graph[nx][ny] == 0:
                        q.append([nx, ny, z - 1])
                        visited[nx][ny][z - 1] = visited[x][y][z] + 1
        for dir in range(4):
            nx, ny, = x + dx[dir], y + dy[dir]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny][z] == -1 and graph[nx][ny] == 0:
                    q.append([nx, ny, z])
                    visited[nx][ny][z] = visited[x][y][z] + 1
    return -1


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
hdx = [-2, -2, -1, -1, 1, 1, 2, 2]
hdy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
print(bfs())