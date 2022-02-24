# 세로 크기 n, 가로 크기 m
n, m = map(int, input().split())

# 방문 위치 저장
visited = [[0] * m for _ in range(n)]

# 로봇 청소기 좌표와 바라보는 방향
x, y, direction = map(int, input().split())

# 현재 좌표 방문 처리
visited[x][y] = 1

# 전체 맵
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서의 좌표 위치 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 로봇 청소기 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 청소한 칸 수 (현재 위치 1번)
count = 1
# 회전 수
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 이동하려는 칸이 청소하지 않았으며 빈칸일 경우
    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        # 해당 칸 청소
        visited[nx][ny] = 1
        # 로봇 청소기 위치 이동
        x, y = nx, ny
        # 청소한 칸 수 증가
        count += 1
        # 회전 횟수 초기화
        turn_time = 0
        continue
    # 그렇지 않을 경우, 회전한 횟수만 1 증가
    else:
        turn_time += 1
    # 네 방향 모두 회전한 후 청소할 구역이 없을 경우
    if turn_time == 4:
        # 후진하는 방향의 x, y 좌표
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 후진이 가능하다면
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 그렇지 않다면
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
