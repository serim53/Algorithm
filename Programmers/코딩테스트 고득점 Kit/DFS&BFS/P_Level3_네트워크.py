def solution(n, computers):
    answer = 0
    networks = [[] for _ in range(n)]
    for i in range(1, n):
        if computers[0][i] == 1:
            networks[0].append(i)

    idx = 0
    for _ in networks[idx]:
        for j in range(idx + 1, n):
            if computers[idx][j] == 1:
                networks[idx].append(j)
        idx += 1

    return networks


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))