from collections import deque

def find_base_camp(store_x, store_y):
    global target_x, target_y
    candidate = []
    min_distance = 2 * n + 1
    isFirst = True
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append([store_x, store_y]) # 좌표, 거리
    visited[store_x][store_y] = 0
    while q:
        x, y = q.popleft()
        if graph[x][y] == 1:
            if isFirst:
                min_distance = visited[x][y]
                candidate.append([x, y])
                isFirst = False
            else:
                if visited[x][y] == min_distance:
                    candidate.append([x, y])
                elif visited[x][y] > min_distance:
                    break
        for dd in range(4):
            nx, ny = x + dx[dd], y + dy[dd]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] < 0 and graph[nx][ny] >= 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    candidate.sort()
    target_x, target_y = candidate[0][0], candidate[0][1]

def move_to_store(u):
    global direction
    visited = [[0] * n for _ in range(n)]
    x, y = user[u]
    store_x, store_y = store[u]
    q = deque()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] >= 0:
            q.append([dir, nx, ny])
            visited[nx][ny] = 1
    while q:
        d, x, y = q.popleft()
        if x == store_x and y == store_y:
            direction = d
            break
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] >= 0 and not visited[nx][ny]:
                q.append([d, nx, ny])
                visited[nx][ny] = 1


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
# 0 : 빈 공간, 1 : 베이스캠프
graph = [list(map(int, input().split())) for _ in range(n)]
basecamp = []   # 베이스캠프 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            basecamp.append([i, j])
basecamp.sort()
store = {}  # 편의점 위치 {key: 사람 번호, value: 원하는 편의점 좌표}
user = {}   # 사람의 위치 {key: 사람 번호, value: 사람 좌표}
for i in range(1, m + 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    store[i] = [x, y]
    graph[x][y] = 2 # 편의점은 2

time = 1
store_blocked = []
basecamp_blocked = []
while store.keys():
    # 1. 격자에 있는 사람들이 편의점 방향을 향해 1칸 움직임
    arrived = []
    for u in user.keys():
        store_x, store_y = store[u]
        direction = -1
        move_to_store(u)
        user_x, user_y = user[u]
        user_x, user_y = user_x + dx[direction], user_y + dy[direction]
        if user_x == store_x and user_y == store_y:
            store_blocked.append([store_x, store_y])
            arrived.append(u)
        else:
            user[u] = user_x, user_y
    # 도착한 사람 빼주기
    for a in arrived:
        store.pop(a)
        user.pop(a)
    for sb in store_blocked:
        sbx, sby = sb
        graph[sbx][sby] = -1
    if time <= m:   # time과 사람 번호가 같음
        store_x, store_y = store[time]
        target_x, target_y = -1, -1
        if basecamp:
            find_base_camp(store_x, store_y)
            user[time] = target_x, target_y
            basecamp_blocked.append([target_x, target_y])
            basecamp.remove([target_x, target_y])
    # 도달한 베캠 못가게 막기 (# 2, # 3)
    for bcb in basecamp_blocked:
        bcbx, bcby = bcb
        graph[bcbx][bcby] = -1
    time += 1
print(time - 1)