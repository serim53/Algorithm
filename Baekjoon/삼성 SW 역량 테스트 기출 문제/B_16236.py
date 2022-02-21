import sys
import collections

dx = (0,0,1,-1)
dy = (1,-1,0,0)
# 시간 (최종 제출)
time = 0
# 아기상어 위치
now_x, now_y = 0, 0
# 아기상어 크기
size = 2
# 물고기 수
fish_cnt = 0
# 물고기 위치
fish_pos = []
# 먹은 물고기 수
eat_cnt = 0


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if 0 < arr[i][j] <= 6:
            fish_cnt += 1
            fish_pos.append((i, j))
        elif arr[i][j] == 9:
            now_x, now_y = i, j
arr[now_x][now_y] = 0

def bfs(now_x, now_y):
    q = collections.deque([(now_x, now_y, 0)])
    dist_list = []
    visited = [[False] * N for _ in range(N)]
    visited[now_x][now_y] = True
    min_dist = int(1e9)
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] <= size:
                    visited[nx][ny] = True
                    if 0 < arr[nx][ny] < size:
                        min_dist = dist
                        dist_list.append((dist + 1, nx, ny))
                    if dist + 1 <= min_dist:
                        q.append((nx, ny, dist + 1))

    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False

while fish_cnt:
    result = bfs(now_x, now_y)
    if not result:
        break
    now_x, now_y = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1
    if size == eat_cnt:
        size += 1
        eat_cnt = 0
    arr[now_x][now_y] = 0
print(time)