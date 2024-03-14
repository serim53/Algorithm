from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 빙산일 경우
                if graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                # 물일 경우
                else:
                    water[x][y] += 1
    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
year = 0

while True:
    num = 0 # 이어진 빙산의 개수
    visited = [[0] * m for _ in range(n)]
    water = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                num += bfs(i, j)
    for i in range(n):
        for j in range(m):
            graph[i][j] -= water[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    if num == 0 or num >= 2:
        break

    year += 1

print(year) if num >= 2 else print(0)