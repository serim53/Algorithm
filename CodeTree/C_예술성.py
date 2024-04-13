from collections import deque

def group_search(x, y):

    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    group[nx][ny] = group_num
                    group_cnt[group_num] += 1
                    q.append((nx, ny))


def art_score():

    score = 0

    for i in range(n):
        for j in range(n):
            for dir in range(4):
                nx = i + dx[dir]
                ny = j + dy[dir]

                if 0 <= nx < n and 0 <= ny < n:
                    if group[nx][ny] != group[i][j]:
                        g_x, g_y = group[i][j], group[nx][ny]
                        g_x_num, g_y_num = graph[i][j], graph[nx][ny]
                        g_x_cnt, g_y_cnt = group_cnt[g_x], group_cnt[g_y]
                        score += (g_x_cnt + g_y_cnt) * g_x_num * g_y_num

    return score // 2


def plus_rotate():
    for i in range(n):
        for j in range(n):
            if i == half:
                arr[i][j] = graph[j][i]
            if j == half:
                arr[i][j] = graph[n - j - 1][n - i - 1]


def square_rotate(x, y):
    for i in range(x, x + half):
        for j in range(y, y + half):
            ox, oy = i - x, j - y
            rx, ry = oy, half - ox - 1
            arr[rx + x][ry + y] = graph[i][j]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

result = 0
for _ in range(4):

    group = [[0] * n for _ in range(n)]
    group_cnt = [0] * (n * n + 1)
    group_num = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_num += 1
                group[i][j] = group_num
                group_cnt[group_num] += 1
                group_search(i, j)

    result += art_score()

    arr = [[0] * n for _ in range(n)]
    half = n // 2

    plus_rotate()

    square_rotate(0, 0)
    square_rotate(0, half + 1)
    square_rotate(half + 1, 0)
    square_rotate(half + 1, half + 1)

    for i in range(n):
        for j in range(n):
            graph[i][j] = arr[i][j]

print(result)
