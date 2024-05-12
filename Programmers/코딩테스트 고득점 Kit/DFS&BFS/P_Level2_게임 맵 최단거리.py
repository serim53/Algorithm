from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[0] * m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[n - 1][m - 1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    return -1