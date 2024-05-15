from collections import deque

def bfs(start, end, maps):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque()

    flag = False
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i, j, 0))
                visited[i][j] = 1
                flag = True
                break
        if flag:
            break

    while q:
        x, y, time = q.popleft()

        if maps[x][y] == end:
            return time

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    q.append((nx, ny, time + 1))
                    visited[nx][ny] = 1
    return -1


def solution(maps):
    result = 0

    path1 = bfs('S', 'L', maps)
    if path1 == -1:
        return -1
    else:
        result += path1

    path2 = bfs('L', 'E', maps)
    if path2 == -1:
        return -1
    else:
        result += path2

    return result