from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
# 벽 부쉈는지 여부 포함
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()


def bfs():
    queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while queue:
        x, y, w = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][w]:
                # 벽이 아닌 경우
                if not graph[nx][ny]:
                    queue.append([nx, ny, w])
                    visited[nx][ny][w] = visited[x][y][w] + 1
                # 벽이 있고 현재 부순 벽이 없는 경우
                if w == 0 and graph[nx][ny] == 1:
                    queue.append([nx, ny, 1])
                    visited[nx][ny][1] = visited[x][y][w] + 1
    return -1


print(bfs())
