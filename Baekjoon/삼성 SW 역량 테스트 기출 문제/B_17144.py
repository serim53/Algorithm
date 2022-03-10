import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())
area = []
for _ in range(r):
    area.append(list(map(int, input().split())))

up, down = -1, -1

# 공기청정기 위치
for i in range(r):
    if area[i][0] == -1:
        up = i
        down = i + 1
        break


# 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    spread_area = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if area[i][j] != 0 and area[i][j] != -1:
                spread_value = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and area[nx][ny] != -1:
                        spread_area[nx][ny] += area[i][j] // 5
                        spread_value += area[i][j] // 5
                area[i][j] -= spread_value

    for i in range(r):
        for j in range(c):
            area[i][j] += spread_area[i][j]


# 공기청정기 - up
def clean_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        area[x][y], before = before, area[x][y]
        x = nx
        y = ny


# 공기청정기 - down
def clean_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        area[x][y], before = before, area[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    clean_up()
    clean_down()

result = 0
for i in range(r):
    for j in range(c):
        if area[i][j] > 0:
            result += area[i][j]

print(result)
