T = int(input())
for test_case in range(1, T + 1):
    result = 0
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 가로
    for i in range(N):
        for j in range(N - K + 1):
            check = 0
            for b in range(j, j + K):
                if arr[i][b]:
                    check += 1
            if check == K:
                if j-1 >= 0 and arr[i][j - 1]:
                    continue
                if j + K < N and arr[i][j + K]:
                    continue
                result += 1
    # 세로
    for i in range(N - K + 1):
        for j in range(N):
            check = 0
            for a in range(i, i + K):
                if arr[a][j]:
                    check += 1
            if check == K:
                if i-1 >= 0 and arr[i - 1][j]:
                    continue
                if i + K < N and arr[i + K][j]:
                    continue
                result += 1

    print('#{} {}'.format(test_case, result))