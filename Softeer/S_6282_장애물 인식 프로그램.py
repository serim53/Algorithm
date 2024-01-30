def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1 and not visited[x][y]:
        global count
        visited[x][y] = 1
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
count = 0
block = 0
obstacle = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            obstacle.append(count)
            block += 1
            count = 0
obstacle.sort()
print(block)
for o in obstacle:
    print(o)