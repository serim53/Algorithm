from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        now_x, now_y = queue.popleft()
        for dir in range(4):
            next_x, next_y = now_x + dx[dir], now_y + dy[dir]
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y]:
                graph[next_x][next_y] = 0
                queue.append((next_x, next_y))
    return

t = int(input())
for _ in range(t):
    # m : 가로, n : 세로, k : 배추가 심어진 위치 개수
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    result = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)