dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
R, C, M = map(int, input().split())
shark = [[[] for _ in range(C)] for _ in range(R)]
result = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[r - 1][c - 1].append([s, d - 1, z])
men = -1
while men < C - 1:
    # 1
    men += 1
    # 2
    for i in range(R):
        if shark[i][men]:
            result += shark[i][men][0][2]
            shark[i][men].clear()
            break
    # 3
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if shark[i][j]:
                s, d, z = shark[i][j][0]
                nx = i + dx[d] * s
                ny = j + dy[d] * s
                while not 0 <= nx < R or not 0 <= ny < C:
                    if 0 > nx:
                        nx = - nx
                        d = 1
                    elif nx >= R:
                        nx = 2 * (R - 1) - nx
                        d = 0
                    elif 0 > ny:
                        ny = -ny
                        d = 2
                    elif ny >= C:
                        ny = 2 * (C - 1) - ny
                        d = 3
                temp[nx][ny].append([s, d, z])
    shark = temp
    for i in range(R):
        for j in range(C):
            if len(shark[i][j]) >= 2:
                power = -1e9
                max_idx = 0
                for k in range(len(shark[i][j])):
                    if shark[i][j][k][2] > power:
                        power = shark[i][j][k][2]
                        max_idx = k
                temp = shark[i][j][max_idx]
                shark[i][j] = [shark[i][j][max_idx]]

print(result)