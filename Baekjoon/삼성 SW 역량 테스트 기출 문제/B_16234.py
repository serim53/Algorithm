from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    num = 0
    united = 1
    global ismove
    queue = deque()
    queue.append((x, y))
    temp = [[x, y]]

    while queue:
        x, y = queue.popleft()
        num += data[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(data[nx][ny] - data[x][y]) <= r and not visited[nx][ny]:
                    visited[x][y] = True
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    temp.append([nx, ny])
                    united += 1
        if united > 1:
            ismove = True
            for x, y in temp:
                data[x][y] = int(num / united)


n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
day = 0

while True:
    ismove = False
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
    if ismove:
        day += 1
    else:
        break

print(data)
print(day)
