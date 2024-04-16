turn = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    move_dir = [[(0, 3), (0, 2), (0, 1)], [(3, 0), (2, 0), (1, 0)],
          [(0, 1), (1, 1), (1, 2)], [(2, -1), (1, -1), (1, 0)],
          [(0, 1), (0, 2), (1, 2)], [(0, 1), (-1, 1), (-2, 1)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (1, 0), (2, 0)],
          [(0, 1), (1, 1), (0, 2)], [(0, 1), (-1, 1), (1, 1)], [(0, 1), (-1, 1), (0, 2)], [(1, 0), (2, 0), (1, 1)],
          [(1, 0), (0, 1), (1, 1)]]

    result = -4000000
    for i in range(n):
        for j in range(n):
            for dir in move_dir:
                sum_num = graph[i][j]
                flag = True
                for d in dir:
                    dx, dy = d
                    nx, ny = i + dx, j + dy
                    if 0 > nx or nx >= n or 0 > ny or ny >= n:
                        flag = False
                        break
                    sum_num += graph[nx][ny]
                if flag and sum_num > result:
                    result = sum_num
    print("{}. {}".format(turn, result))
    turn += 1