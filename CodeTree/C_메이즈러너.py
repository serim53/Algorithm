def rotate(size, start_x, start_y):
    # 기본 그래프 회전
    global exit_x, exit_y
    new = [[0] * size for _ in range(size)]
    print(size, start_x, start_y)
    for i in range(start_x, start_x + size):
        for j in range(start_y, start_y + size):
            new[j - start_y][size - (i - start_x) - 1] = graph[i][j]
    print("---new---")
    for n2 in new:
        print(n2)
    for i in range(start_x, start_x + size):
        for j in range(start_y, start_y + size):
            graph[i][j] = new[i - start_x][j - start_y]
            if graph[i][j] == 11:   # 출구
                exit_x, exit_y = i, j
            elif graph[i][j] > 0:
                graph[i][j] -= 1

    # 유저 그래프 회전
    new_user = [[0] * size for _ in range(size)]
    for i in range(start_x, start_x + size):
        for j in range(start_y, start_y + size):
            new_user[j - start_y][size - (i - start_x) - 1] = user_graph[i][j]
    for i in range(start_x, start_x + size):
        for j in range(start_y, start_y + size):
            user_graph[i][j] = new_user[i - start_x][j - start_y]

def find_direction_and_move(x, y):
    print("x :", x, "y :", y)
    global num_move, users
    min_dist = abs(x - exit_x) + abs(y - exit_y) - 1
    direction = -1
    # 방향 찾기
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and (graph[nx][ny] == 0 or graph[nx][ny] == 11):
            temp_dist = abs(nx - exit_x) + abs(ny - exit_y)
            if min_dist >= temp_dist:
                direction = dir
                min_dist = temp_dist
    print(direction)
    # 이동하기
    if direction != -1:
        num_move += -user_graph[x][y]
        nx, ny = x + dx[direction], y + dy[direction]
        if nx == exit_x and ny == exit_y:
            print("출구야")
            users -= -user_graph[x][y]
        else:
            print("아니야")
            user_graph[nx][ny] += user_graph[x][y]
        user_graph[x][y] = 0
    print("이동 직후")
    for u in user_graph:
        print(u)
    print("num", num_move)

def find_rectangle():
    print("find_rectangle")
    global r_x, r_y, r_size
    for size in range(2, n + 1):
        for start_x in range(n - size + 1):
            for start_y in range(n - size + 1):
                end_x, end_y = start_x + size - 1, start_y + size - 1
                if not (start_x <= exit_x <= end_x and start_y <= exit_y <= end_y):
                    continue
                is_user_in = False
                for i in range(start_x, end_x + 1):
                    for j in range(start_y, end_y + 1):
                        if user_graph[i][j] < 0:
                            is_user_in = True
                            break
                if is_user_in:
                    r_x, r_y, r_size = start_x, start_y, size
                    print("r_x", r_x, r_y, r_size)
                    return

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
user_graph = [[0] * n for _ in range(n)]
users = m
for i in range(1, m + 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    user_graph[x][y] = -1

exit_x, exit_y = map(int, input().split())
exit_x, exit_y = exit_x - 1, exit_y - 1
graph[exit_x][exit_y] = 11  #   출구는 11
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
num_move = 0
r_x, r_y,r_size = 0, 0, 0

while k and m:

    print(k, "번 ------")
    # 참가자가 방향 찾고 움직이기
    users_to_move = []
    for i in range(n):
        for j in range(n):
            if user_graph[i][j] < 0:
                users_to_move.append([i, j])
    for i, j in users_to_move:
        find_direction_and_move(i, j)
    print("참가자 이동 후")
    for u in user_graph:
        print(u)
    find_rectangle()
    rotate(r_size, r_x, r_y)
    print("회전 후 기본 그래프")
    for g in graph:
        print(g)
    print("회전 후 참가자 그래프")
    for u in user_graph:
        print(u)
    k -= 1

print(num_move)
print(exit_x + 1, exit_y + 1)