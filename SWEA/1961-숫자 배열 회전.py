t = int(input())
for test_case in range(1, t + 1):

    n = int(input())
    origin = [list(map(int, input().split())) for _ in range(n)]
    rotate_90 = [[0 for _ in range(n)] for _ in range(n)]
    rotate_180 = [[0 for _ in range(n)] for _ in range(n)]
    rotate_270 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotate_90[i][j] = origin[n - 1 - j][i]

    for i in range(n):
        for j in range(n):
            rotate_180[i][j] = rotate_90[n - 1 - j][i]

    for i in range(n):
        for j in range(n):
            rotate_270[i][j] = rotate_180[n - 1 - j][i]

    print('#{}'.format(test_case))
    for i in range(n):
        for a in range(n):
            print(rotate_90[i][a], end='')
        print(end=' ')
        for b in range(n):
            print(rotate_180[i][b], end='')
        print(end=' ')
        for c in range(n):
            print(rotate_270[i][c], end='')
        print()