T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            now = 0
            for k in range(M):
                for l in range(M):
                    now += arr[i + k][j + l]
            if now > result:
                result = now
    print('#{} {}'.format(test_case, result))