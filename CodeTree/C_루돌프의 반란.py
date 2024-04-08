def get_distance(sx, sy, ex, ey):
    return (sx - ex) ** 2 + (sy - ey) ** 2

def interaction(new, x, y, direction, isSanta):
    num = new
    while 0 <= x < n and 0 <= y < n and graph[x][y] != 0:
        new = num
        num = graph[x][y]   # 기존 산타 저장
        graph[x][y] = new
        num_santa[new] = [x, y]
        if isSanta:
            x, y = x - sdx[direction], y - sdy[direction]
        else:
            x, y = x + rdx[direction], y + rdy[direction]
    if 0 <= x < n and 0 <= y < n:
        graph[x][y] = num
        num_santa[num] = [x, y]
    else:
        num_santa.pop(num)

def move_rudolf():
    global rr, rc
    # 목표 구하기
    min_dist = 1e9
    target_x, target_y = -1, -1
    for i in range(n):
        for j in range(n):
            if 1 <= graph[i][j] <= p:
                dist = get_distance(rr, rc, i, j)
                if dist <= min_dist:
                    min_dist = dist
                    target_x, target_y = i, j
    # 이동 방향 정하기
    direction = -1
    for dir in range(8):
        nrx, nry = rr + rdx[dir], rc + rdy[dir]
        if 0 <= nrx < n and 0 <= nry < n:
            dist = get_distance(nrx, nry, target_x, target_y)
            if dist <= min_dist:
                min_dist = dist
                direction = dir

    # 이동하기
    graph[rr][rc] = 0
    rr, rc = rr + rdx[direction], rc + rdy[direction]
    num = graph[rr][rc]
    # 충돌 발생
    if num > 0:
        score[num] += c # 산타 점수 부여
        # 산타 밀리는 중 상호작용 발생
        sx, sy = rr + c * rdx[direction], rc + c * rdy[direction]   # 산타 충돌 후 이동 지점
        if 0 > sx or sx >= n or 0 > sy or sy >= n:
            num_santa.pop(num)  # 산타 게임 탈락
        elif graph[sx][sy] > 0:
            interaction(num, sx, sy, direction, False)
            status[num] = 2  # 산타 기절
        else:
            graph[sx][sy] = num
            num_santa[num] = [sx, sy]
            status[num] = 2 # 산타 기절
    graph[rr][rc] = 31

def move_santa():
    for i in range(1, p + 1):
        if i in num_santa.keys() and i not in status.keys(): # 기절 상태가 아니라면
            x, y = num_santa[i]
            direction = -1
            dist = get_distance(x, y, rr, rc)
            # 이동 방향 구하기
            for dir in range(3, -1, -1):
                nx, ny = x + sdx[dir], y + sdy[dir]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] not in [i for i in range(1, p + 1)]:
                    if get_distance(nx, ny, rr, rc) <= dist:
                        dist = get_distance(nx, ny, rr, rc)
                        direction = dir
            # 이동할 수 있는 곳이 있다면
            if direction != -1:
                nx, ny = x + sdx[direction], y + sdy[direction]
                graph[x][y] = 0
                # 이동한 곳에 루돌프가 있다면 충돌
                if graph[nx][ny] == 31:
                    score[i] += d
                    # 밀려남
                    nnx, nny = nx - d * sdx[direction], ny - d * sdy[direction]
                    if 0 > nnx or nnx >= n or 0 > nny or nny >= n:
                        num_santa.pop(i)  # 산타 게임 탈락
                    elif graph[nnx][nny] > 0:
                        interaction(i, nnx, nny, direction, True)
                        status[i] = 2
                    else:
                        graph[nnx][nny] = i
                        num_santa[i] = [nnx, nny]
                        status[i] = 2
                else:
                    graph[nx][ny] = i
                    num_santa[i] = [nx, ny]


n, m, p, c, d = map(int, input().split())
graph = [[0] * n for _ in range(n)]
rr, rc = map(int, input().split())
rr, rc = rr - 1, rc - 1
# 루돌프 31번
graph[rr][rc] = 31
num_santa = {}
for _ in range(p):
    num, sr, sc = map(int, input().split())
    graph[sr - 1][sc - 1] = num
    num_santa[num] = [sr - 1, sc - 1]
score = [0] * (p + 1)
# 기절 상태 저장
status = {}
rdx = [-1, 1, 0, 0, -1, -1, 1, 1]
rdy = [0, 0, -1, 1, -1, 1, -1, 1]
# 상우하좌
sdx = [-1, 0, 1, 0]
sdy = [0, 1, 0, -1]
while m and len(num_santa.keys()):
    move_rudolf()
    move_santa()
    for i in num_santa.keys():
        score[i] += 1
    nums_pop = []
    for i in status.keys():
        status[i] -= 1
        if status[i] == 0:
            nums_pop.append(i)
    for i in nums_pop:
        status.pop(i)
    m -= 1
print(' '.join(str(i) for i in score[1:]))