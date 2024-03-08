from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def spread():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != '#' and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    fire.append((nx, ny))


def move():
    flag = False
    for _ in range(len(q)):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == 0 and graph[nx][ny] != '#' and graph[nx][ny] != '*':
                    flag = True
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
            else:
                return visited[x][y]
    if not flag:
        return 'IMPOSSIBLE'


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    graph = []
    fire = deque()
    q = deque()
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        graph.append(list(input().strip()))
        for j in range(w):
            if graph[i][j] == '*':
                fire.append((i, j))
            if graph[i][j] == '@':
                q.append((i, j))
                visited[i][j] = 1

    result = 0
    while True:
        spread()
        result = move()
        if result:
            break

    print(result)