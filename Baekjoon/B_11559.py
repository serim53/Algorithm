from collections import deque

def fall():
    for y in range(6):
        for x in range(10, -1, -1):
            for fall_point in range(11, x, -1):
                if graph[x][y] != '.' and graph[fall_point][y] == '.':
                    graph[fall_point][y] = graph[x][y]
                    graph[x][y] = '.'

def burst(i, j, color):
    global flag
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    blocks = [[i, j]]
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == color and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = 1
                blocks.append([nx, ny])
    if len(blocks) >= 4:
        flag = True
        for x, y in blocks:
            graph[x][y] = '.'

graph = [list(input().rstrip()) for _ in range(12)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0

while True:
    flag = False
    visited = [[0] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                burst(i, j, graph[i][j])

    if flag:
        fall()
        result += 1
    else:
        break

print(result)