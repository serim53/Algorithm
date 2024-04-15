import heapq

def dijkstra(i, j):
    q = []
    heapq.heappush(q, (graph[i][j], i, j))
    visited[i][j] = graph[i][j]
    while q:
        cnt, x, y = heapq.heappop(q)
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 1e9:
                cnt_lose = cnt + graph[nx][ny]
                if cnt_lose < visited[nx][ny]:
                    visited[nx][ny] = cnt_lose
                    heapq.heappush(q, (cnt_lose, nx, ny))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
turn = 0
while True:
    turn += 1
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[1e9] * n for _ in range(n)]
    dijkstra(0, 0)
    print("Problem {}: {}".format(turn, visited[n - 1][n - 1]))