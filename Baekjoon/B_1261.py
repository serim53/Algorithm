import heapq

def dijkstra(i, j):
    global result
    q = []
    heapq.heappush(q, (0, i, j))
    visited[i][j] = 1
    distance[i][j] = 0
    while q:
        cnt, x, y = heapq.heappop(q)
        if x == n - 1 and y == m - 1:
            result = min(cnt, result)
        if distance[x][y] < cnt: continue
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                cnt_break = cnt + int(graph[nx][ny])
                if cnt_break < distance[nx][ny]:
                    distance[nx][ny] = cnt_break
                    heapq.heappush(q, (cnt_break, nx, ny))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m, n = map(int, input().split())
graph = [list(input()) for _ in range(n)]
distance = [[1e9] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = n * m
dijkstra(0, 0)
print(result)