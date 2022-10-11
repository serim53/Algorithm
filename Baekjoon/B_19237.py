n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))
# 상어의 방향별 우선순위 (상, 하, 좌, 우)
priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

smell = [[[0, 0]] * n for _ in range(n)]


def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if area[i][j] != 0:
                smell[i][j] = [area[i][j], k]


def move():
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] != 0:
                direction = directions[area[i][j] - 1]
                found = False
                for idx in priorities[area[i][j] - 1][direction - 1]:
                    nx = i + dx[idx - 1]
                    ny = j + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            directions[area[i][j] - 1] = idx
                            if temp[nx][ny] == 0:
                                temp[nx][ny] = area[i][j]
                            else:
                                temp[nx][ny] = min(area[i][j], temp[nx][ny])
                            found = True
                            break
                if found:
                    continue

                for idx in priorities[area[i][j] - 1][direction - 1]:
                    nx = i + dx[idx - 1]
                    ny = j + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == area[i][j]:
                            directions[area[i][j] - 1] = idx
                            temp[nx][ny] = area[i][j]
                            break
    return temp


result = 0
while True:
    update_smell()
    temp = move()
    area = temp
    result += 1

    check = True
    for i in range(n):
        for j in range(n):
            if area[i][j] > 1:
                check = False
    if check:
        print(result)
        break

    if result >= 1000:
        print(-1)
        break