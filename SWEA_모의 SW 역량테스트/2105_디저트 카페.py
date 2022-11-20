import sys
sys.stdin = open("input.txt", "r")


def dfs(x, y, path, way):
    global result, i, j

    if way == 3 and x == i and y == j and len(path) > 2:
        result = max(result, len(path))
        return
거
    if 0 <= x < n and 0 <= y < n and board[x][y] not in path:
        new_path = path + [board[x][y]]
        nx, ny = x + dir[way][0], y + dir[way][1]
        dfs(nx, ny, new_path, way)

        if way < 3:
            nx, ny = x + dir[way + 1][0], y + dir[way + 1][1]
            dfs(nx, ny, new_path, way + 1)

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    result = -1
    for i in range(n):
        for j in range(n):
            dfs(i, j, [], 0)

    print('#{} {}'.format(tc, result))