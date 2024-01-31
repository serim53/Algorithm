import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[0, 0]])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    visited[nx][ny] += 1

                elif visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                graph[i][j] = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while True:
    if graph.count(graph[0]) == n:
        break

    visited = [[0] * m for _ in range(n)]
    bfs()
    cnt += 1

print(cnt)