import sys
from collections import deque
input = sys.stdin.readline

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, k):
    visited[x][y] = 1
    q.append([x, y])
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == k:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    return cnt


n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 2, 3, 4, 5, 6]
x, y, dir, ans = 0, 0, 0, 0

for _ in range(k):
    if not 0 <= x + dx[dir] < n or not 0 <= y + dy[dir] < m:
        dir = (dir + 2) % 4

    x, y = x + dx[dir], y + dy[dir]

    q = deque()
    visited = [[0] * m for _ in range(n)]

    ans += (bfs(x, y, graph[x][y]) + 1) * graph[x][y]

    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif dir == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    if dice[5] > graph[x][y]:
        dir = (dir + 1) % 4
    elif dice[5] < graph[x][y]:
        dir = (dir + 3) % 4

print(ans)