def dfs(length, visited, x, y, used):
    global max_len
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] < graph[x][y]:
                visited[nx][ny] = True
                dfs(length + 1, visited, nx, ny, used)
                visited[nx][ny] = False
            elif graph[nx][ny] >= graph[x][y] and not used:
                used = True
                for j in range(1, k + 1):
                    graph[nx][ny] -= j
                    if graph[nx][ny] < graph[x][y]:
                        visited[nx][ny] = True
                        dfs(length + 1, visited, nx, ny, used)
                        visited[nx][ny] = False
                    graph[nx][ny] += j
                used = False

    if length > max_len:
        max_len = length
t = int(input())
for tc in range(1, t + 1):
    # 지도 한 변의 길이, 최대 공사 가능 깊이
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    max_len = -1e9
    maxs = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == max(map(max, graph)):
                maxs.append([i, j])
    for m in maxs:
        visited[m[0]][m[1]] = True
        dfs(1, visited, m[0], m[1], False)
        visited[m[0]][m[1]] = False

    print("#{} {}".format(tc, max_len))