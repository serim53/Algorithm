from collections import deque

n, m = 0, 0
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j, maps):
    cnt = int(maps[i][j])
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    cnt += int(maps[nx][ny])
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    return cnt


def solution(maps):
    global n, m, visited
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j, maps))
    if answer:
        return sorted(answer)
    else:
        return [-1]