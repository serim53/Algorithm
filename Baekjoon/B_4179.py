from collections import deque

def bfs():
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if not f_visited[nx][ny] and maze[nx][ny] != "#":
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx, ny))
    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0<= ny < c:
                if not j_visited[nx][ny] and maze[nx][ny] != "#":
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y]
                        j_queue.append((nx, ny))
            else:
                return j_visited[x][y] + 1
    return "IMPOSSIBLE"

r, c = map(int, input().split())
maze = [list(input().split()) for _ in range(r)]
f_queue, j_queue = deque(), deque()
f_visited, j_visited = [[0] * c for _ in  range(r)], [[0] * c for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if maze[i][j] == "J":
            j_queue.append((i, j))
        elif maze[i][j] == "F":
            f_queue.append((i, j))

