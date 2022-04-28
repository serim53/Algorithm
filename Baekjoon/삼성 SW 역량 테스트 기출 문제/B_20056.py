n, m, k = map(int, input().split())
# r, c, m, s, d
balls = [list(map(int, input().split())) for _ in range(m)]
graph = [[[] for _ in range(n)] for _ in range(n)]
# 행 x, 열 y
direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

result =0

for _ in range(k):
    while balls:
        cr, cc, cm, cs, cd = balls.pop(0)
        nr = (cr + direction[cd][0] * cs) % n
        nc = (cc + direction[cd][1] * cs) % n
        graph[nr][nc].append([cm, cs, cd])

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 2:
                mass, speed, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[i][j])
                for b in graph[i][j]:
                    mass += b[0]
                    speed += b[1]
                    if b[2] % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt_even == cnt:
                    d = [0, 2, 4, 6]
                else:
                    d = [1, 3, 5, 7]
                if mass // 5:
                    for _d in d:
                        balls.append([i, j, mass//5, speed/len(graph[i][j]), _d])

            if len(graph[i][j]) == 1:
                balls.append([i, j] + graph[i][j].pop())



print(sum([b[2] for b in balls]))