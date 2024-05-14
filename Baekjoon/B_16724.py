def move(x, y, idx):
    global result
    if visited[x][y] != -1:
        if visited[x][y] == idx:
            result += 1
        return
    visited[x][y] = idx
    i = direction.index(graph[x][y])
    move(x + dx[i], y + dy[i], idx)


n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
idx = 0
result = 0
for i in range(n):
    for j in range(m):
        move(i, j, idx)
        idx += 1

print(result)