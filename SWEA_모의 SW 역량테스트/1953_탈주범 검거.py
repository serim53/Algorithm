from collections import deque
import sys
sys.stdin = open("input.txt", "r")

pipe = [[],
        [[0, 1], [0, -1], [1, 0], [-1, 0]],
        [[1, 0], [-1, 0]],
        [[0, 1], [0, -1]],
        [[0, 1], [-1, 0]],
        [[0, 1], [1, 0]],
        [[0, -1], [1, 0]],
        [[0, -1], [-1, 0]]]
t = int(input())
for tc in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    queue = deque([[r, c]])
    visited[r][c] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in pipe[graph[x][y]]:
            nx = x + dx
            ny = y + dy
            if not 0 <= nx < n or not 0 <= ny < m:
                continue
            if [-dx, -dy] in pipe[graph[nx][ny]]:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue += [[nx, ny]]
                    if visited[nx][ny] <= l:
                        cnt += 1

    print("#{} {}".format(tc, cnt))