def dfs(x, y, cnt, const):
    global result
    if result < cnt:
        result = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 1:
            continue
        if graph[x][y] > graph[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, const)
            visited[nx][ny] = 0
        elif graph[x][y] <= graph[nx][ny] and not const:
            for j in range(1, k + 1):
                graph[nx][ny] -= j
                const = True
                if graph[x][y] > graph[nx][ny]:
                    visited[nx][ny] = 1
                    dfs(nx, ny, cnt + 1, const)
                    visited[nx][ny] = 0
                const = False
                graph[nx][ny] += j

test_case = int(input())
for tc in range(1, test_case + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    visited = [[0] * n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_height = 0
    for i in range(n):
        for j in range(n):
            if max_height < graph[i][j]:
                max_height = graph[i][j]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == max_height:
                visited[i][j] = 1
                dfs(i, j, 1, False)
                visited[i][j] = 0

    print("#{} {}".format(tc, result))
