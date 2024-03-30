from collections import deque

def find_island(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    graph[i][j] = island_num
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] and not visited[nx][ny]:
                graph[nx][ny] = island_num
                q.append([nx, ny])
                visited[nx][ny] = 1

def find_other_island(num):
    q = deque()
    distance = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                q.append([i, j])
                distance[i][j] = 0
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and  0 <= ny < n:
                if graph[nx][ny] != num and graph[nx][ny]:
                    return distance[x][y]
                if not graph[nx][ny] and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append([nx, ny])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
island_num = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            find_island(i, j)
            island_num += 1
result = 10001
for num in range(1, island_num):
    result = min(result, find_other_island(num))
print(result)