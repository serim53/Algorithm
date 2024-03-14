from collections import deque

def bfs(i, j, flag, visited):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    color = graph[i][j]
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if (color == 'R' or color == 'G') and flag:
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                else:
                    if graph[nx][ny] == color:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
    return 1


n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
rg_visited = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
rg_result = 0
# 적록색약이 아닌 사람
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result += bfs(i, j, False, visited)
# 적록색약인 사람
for i in range(n):
    for j in range(n):
        if not rg_visited[i][j]:
            rg_result += bfs(i, j, True, rg_visited)
print(result, rg_result)