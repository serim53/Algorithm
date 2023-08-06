from collections import deque
from itertools import combinations


def bfs(active):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    for a in active:
        x, y = a
        q.append(a)
        visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if area[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    for i in range(n):
        for j in range(n):
            if area[i][j] == 0 and visited[i][j] == -1:
                return -1
    return max(max(v) for v in visited)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
virus = []
result = 1e9
for i in range(n):
    for j in range(n):
        if area[i][j] == 2:
            virus.append([i, j])
for com in combinations(virus, m):
    result = min(result, bfs(com))

print(result)