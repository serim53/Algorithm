from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(land, row, col):
    global n, m, visited, num, oils
    q = deque([(row, col)])
    cnt = 1
    visited[row][col] = 1
    land[row][col] = num
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
                land[nx][ny] = num
                q.append([nx, ny])
    oils[num] = cnt
    num += 1

def solution(land):
    global n, m, visited, num, oils
    num, oils, answer = 1, {}, 0
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                bfs(land, i, j)
    for j in range(m):
        s = set()
        temp = 0
        for i in range(n):
            if land[i][j]:
                s.add(land[i][j])
        for o in s:
            temp += oils[o]
        if answer < temp:
            answer = temp
    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
