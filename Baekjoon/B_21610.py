def diagonal(i, j):
    global area
    num = 0
    # 좌측 상단 대각선
    if i >= 1 and j >= 1 and area[i - 1][j - 1] > 0:
        num += 1
    # 우측 상단 대각선
    if i >= 1 and j < n - 1 and area[i - 1][j + 1] > 0:
        num += 1
    # 좌측 하단 대각선
    if i < n - 1 and j >= 1 and area[i + 1][j - 1] > 0:
        num += 1
    # 우측 하단 대각선
    if i < n - 1 and j < n - 1 and area[i + 1][j + 1] > 0:
        num += 1
    area[i][j] += num
    print("dia")
    print("-------")
    for a in area:
        print(a)

def move(d, s):
    global cloud, area
    temp = [c[:] for c in cloud]
    for t in temp:
        print("i", t)
        x = t[0]
        y = t[1]
        x += s * dx[d - 1]
        y += s * dy[d - 1]

        area[x % n][y % n] += 1

        t = [x % n, y % n]

        print("change i", t)
        print("------")
        for a in area:
            print(a)

    for t in temp:
        diagonal(t[0], t[1])

    cloud.clear()

    for _x in range(n):
        for _y in range(n):
            if area[_x][_y] >= 2 and [_x, _y] not in temp:
                cloud.append([_x, _y])
                area[_x][_y] -= 2

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
info = [list(map(int, input().split())) for _ in range(m)]
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
result = 0

# 방향, 거리
for i in info:
    d, s = i
    move(d, s)
    print(area)
    print("cloud", cloud)

for i in range(n):
    for j in range(n):
        result += area[i][j]

print(result)