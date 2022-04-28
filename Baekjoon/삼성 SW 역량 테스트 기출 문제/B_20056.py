n, m, k = map(int, input().split())
balls = []
# r, c, m, s, d
# balls = [list(map(int, input().split())) for _ in range(m)]
for _ in range(m):
    _r, _c, _m, _s, _d = list(map(int, input().split()))
    balls.append([_r-1, _c-1, _m, _s, _d])
graph = [[[] for _ in range(n)] for _ in range(n)]
# 행 x, 열 y

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    while balls:
        cr, cc, cm, cs, cd = balls.pop(0)
        nr = (cr + cs * dx[cd]) % n  # 1번-N번 행 연결되어있기 때문
        nc = (cc + cs * dy[cd]) % n
        graph[nr][nc].append([cm, cs, cd])

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 2:
                mass, speed, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    _m, _s, _d = graph[i][j].pop(0)
                    mass += _m
                    speed += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    d = [0, 2, 4, 6]
                else:
                    d = [1, 3, 5, 7]
                if mass // 5:
                    for dd in d:
                        balls.append([i, j, mass//5, speed//cnt, dd])

            if len(graph[i][j]) == 1:
                balls.append([i, j] + graph[i][j].pop())



print(sum([b[2] for b in balls]))