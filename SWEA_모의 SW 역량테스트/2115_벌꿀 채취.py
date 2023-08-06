from itertools import combinations
t = int(input())
for tc in range(1, t + 1):
    # 벌통 크기, 벌통 개수, 채취할 수 있는 최대 꿀 양
    n, m, c = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(n)]
    result = -1e9
    for i in range(n):
        for j in range(n):
            # 한 라인에 두 개가 있을 경우
            if i == j:
                pass
            # 두 라인에 하나씩 있을 경우
            else:
                pass
    # if n >= m * 2:
    #     for i in range(0, n - m):
    #         for j in range(i + 1, n - 2):
    #             honey_a = infos[i::i + m]
    #             honey_b = infos[j::j + m]
    #             for k in range(1, m + 1):
    #                 combi = combinations(honey_a, k)
    #                 if sum(combi) <= c:
    #                     for j in combi:
    #
    #
    # # 두 라인에 하나씩 있을 경우
    # for lines in combinations([i for i in range(0, n)], 2):

