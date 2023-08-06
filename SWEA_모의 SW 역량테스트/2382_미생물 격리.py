dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
rev = (0, 2, 1, 4, 3)

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    A = []
    for _ in range(K):
        A.append(list(map(int, input().split())))

    for _ in range(M):
        info = dict()
        for row in range(K):
            r, c, k, d = A[row]
            if not k:
                continue
            nr = r + dr[d]

            nc = c + dc[d]
            A[row][0], A[row][1] = nr, nc
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                A[row][2] //= 2
                A[row][3] = rev[d]
            if (nr, nc) not in info.keys():
                info[(nr, nc)] = [row, k]
            else:
                num, size = info[(nr, nc)]
                if A[row][2] > size:
                    info[(nr, nc)] = [row, A[row][2]]
                    A[row][2] += A[num][2]
                    A[num][2] = 0
                else:
                    A[num][2] += A[row][2]
                    A[row][2] = 0
    microbe = 0
    for m in A:
        microbe += m[2]
    print("#{} {}".format(tc+1, microbe))