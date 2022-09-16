from itertools import combinations, permutations
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    min_diff = 1e9
    for num1 in combinations([i for i in range(1, n + 1)], n // 2):
        flavor1, flavor2 = 0, 0
        num2 = [i for i in range(1, n + 1) if i not in num1]
        perm_num1 = list(permutations(num1, 2))
        perm_num2 = list(permutations(num2, 2))
        for p in perm_num1:
            flavor1 += synergy[p[0] - 1][p[1] - 1]
        for p2 in perm_num2:
            flavor2 += synergy[p2[0] - 1][p2[1] - 1]
        diff = abs(flavor1 - flavor2)
        if diff < min_diff:
            min_diff = diff
    print("#{} {}".format(tc, min_diff))