def check_and_attach():
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    for dir in range(4):
        for i in range(n - r + 1):
            for j in range(m - c + 1):
                if check(r, c, sticker, i, j):
                    attach(r, c, sticker, i, j)
                    return
        # rotate
        sticker = list(map(list, zip(*sticker[::-1])))
        r, c = c, r
    return

def check(r, c, sticker, start_x, start_y):
    for x in range(r):
        for y in range(c):
            if sticker[x][y] and graph[start_x + x][start_y + y]:
                return False
    return True

def attach(r, c, sticker, start_x, start_y):
    for i in range(r):
        for j in range(c):
            if sticker[i][j]:
                graph[i + start_x][j + start_y] = 1

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    check_and_attach()
result = 0
for i in range(n):
    result += sum(graph[i])
print(result)