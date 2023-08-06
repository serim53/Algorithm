# 사이클을 확인하는 함수
def check(start_x, start_y, color, x, y, cnt):
    global result
    if result is True:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 게임판을 벗어나면 넘어감
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 사이클 완성 - 공이 4개 이상 + 처음 공으로 돌아옴
        if cnt >= 4 and nx == start_x and ny == start_y:
            result = True
            return
        # 사이클 내 포함될 수 있는 공일 경우
        if graph[nx][ny] == color and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            check(start_x, start_y, color, nx, ny, cnt + 1)
            visited[nx][ny] = 0


# 실제 게임을 실행하고 결과를 출력하는 함수
def run():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            check(i, j, graph[i][j], i, j, 1)
            if result:
                return 'Yes'
    return 'No'


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = False

print(run())
