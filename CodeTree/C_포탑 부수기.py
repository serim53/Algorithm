from collections import deque

def put_attacker_info(x, y):
    global attacker_x, attacker_y, attacker_min_power, attacker_time
    attacker_min_power = graph[x][y][0]
    attacker_time = graph[x][y][1]
    attacker_x, attacker_y = x, y

def put_target_info(x, y):
    global target_x, target_y, target_max_power, target_time
    target_max_power = graph[x][y][0]
    target_time = graph[x][y][1]
    target_x, target_y = x, y

def select_attacker():
    for j in range(m):
        for i in range(n):
            if graph[i][j][0]:
                if graph[i][j][0] < attacker_min_power:
                    put_attacker_info(i, j)
                elif graph[i][j][0] == attacker_min_power:
                    if graph[i][j][1] > attacker_time:
                        put_attacker_info(i, j)
                    elif graph[i][j][1] == attacker_time:
                        if i + j >= attacker_x + attacker_y:
                            put_attacker_info(i, j)
    graph[attacker_x][attacker_y][0] += (n + m)

def select_target():
    for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if graph[i][j][0] and not (i == attacker_x and j == attacker_y):
                if graph[i][j][0] > target_max_power:
                    put_target_info(i, j)
                elif graph[i][j][0] == target_max_power:
                    if graph[i][j][1] < target_time:
                        put_target_info(i, j)
                    elif graph[i][j][1] == target_time:
                        if i + j <= target_x + target_y:
                            put_target_info(i, j)

def lazer_lower_top_power(tops):
    global num_tops
    # 근처 탑들 공격
    power = graph[attacker_x][attacker_y][0] // 2
    for top in tops:
        tx, tw = top
        graph[tx][tw][0] -= power
        if graph[tx][tw][0] <= 0:
            graph[tx][tw][0] = 0
            num_tops -= 1
    # 타겟 탑 공격
    graph[target_x][target_y][0] -= graph[attacker_x][attacker_y][0]
    if graph[target_x][target_y][0] <= 0:
        graph[target_x][target_y][0] = 0
        num_tops -= 1
    # 공격자 시간 갱신
    graph[attacker_x][attacker_y][1] = time

    # 포탑 정비
    for i in range(n):
        for j in range(m):
            if [i, j] not in tops and graph[i][j][0] > 0:
                if [i, j] not in [[attacker_x, attacker_y], [target_x, target_y]]:
                    graph[i][j][0] += 1

def lazer_attack():
    global lazer_attacked
    # 우/하/좌/상 우선순위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[[]] * m for _ in range(n)]
    q = deque()
    q.append([attacker_x, attacker_y])
    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            lazer_attacked = True
            lazer_lower_top_power(visited[x][y][1:])
            return
        for dir in range(4):
            nx, ny = (x + dx[dir]) % n, (y + dy[dir]) % m
            if not visited[nx][ny] and graph[nx][ny][0] > 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + [[x, y]]

def bomb_lower_top_power():
    global num_tops
    dir_x = [0, 0, 1, -1, -1, -1, 1, 1]
    dir_y = [1, -1, 0, 0, -1, 1, -1, 1]
    attacked_top = []
    # 근처 탑들 공격
    power = graph[attacker_x][attacker_y][0] // 2
    for dir in range(8):
        nx, ny = (target_x + dir_x[dir]) % n, (target_y + dir_y[dir]) % m
        if not (nx == attacker_x and ny == attacker_y) and graph[nx][ny][0] > 0:
            graph[nx][ny][0] -= power
            if graph[nx][ny][0] <= 0:
                graph[nx][ny][0] = 0
                num_tops -= 1
            attacked_top.append([nx, ny])
    # 타겟 탑 공격
    graph[target_x][target_y][0] -= graph[attacker_x][attacker_y][0]
    if graph[target_x][target_y][0] <= 0:
        graph[target_x][target_y][0] = 0
        num_tops -= 1
    # 공격자 시간 갱신
    graph[attacker_x][attacker_y][1] = time

    # 포탑 정비
    for i in range(n):
        for j in range(m):
            if [i, j] not in attacked_top and graph[i][j][0] > 0:
                if [i, j] not in [[attacker_x, attacker_y], [target_x, target_y]]:
                    graph[i][j][0] += 1


n, m, k = map(int, input().split())
input_graph = [list(map(int, input().split())) for _ in range(n)]
graph = [[[]] * m for _ in range(n)]

num_tops = 0    # 남은 포탑 수
for i in range(n):
    for j in range(m):
        if input_graph[i][j] != 0:
            num_tops += 1
        graph[i][j] = [input_graph[i][j], 0]  # [공격력, 최근 공격 시점]

time = 1
while time <= k:
    if num_tops == 1:
        break
    # 공격자 선정을 위한 정보
    attacker_x, attacker_y = -1, -1
    attacker_min_power = 5001
    attacker_time = k + 1
    # 타겟 선정을 위한 정보
    target_x, target_y = -1, -1
    target_max_power = 0
    target_time = -1

    lazer_attacked = False
    select_attacker()   # 공격자 선정
    select_target()   # 타겟 선정
    lazer_attack()
    if not lazer_attacked:
        bomb_lower_top_power()
    time += 1


max_power = 0
for i in range(n):
    for j in range(m):
        if graph[i][j][0] > max_power:
            max_power = graph[i][j][0]
print(max_power)