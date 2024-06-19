from collections import deque

def solution(board):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    n = len(board)
    m = len(board[0])
    q = deque()
    visited = [[987654321 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                visited[i][j] = 0
                break

    while q:
        x, y, dist = q.popleft()

        if board[x][y] == 'G':
            return dist

        for i in range(4):
            nx, ny = x, y

            while 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < m and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]

            if visited[nx][ny] > dist + 1:
                visited[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))

    return -1