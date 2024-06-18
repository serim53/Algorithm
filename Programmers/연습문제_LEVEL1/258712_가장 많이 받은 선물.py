def solution(friends, gifts):
    nums = {}
    len_friends = len(friends)
    for i in range(len_friends):
        nums[friends[i]] = i
    given_infos = [[0] * len_friends for _ in range(len_friends)]
    degree = {}
    for i in range(len_friends):
        degree[i] = 0
    for gift in gifts:
        a, b = map(str, gift.split())
        a, b = nums[a], nums[b]
        given_infos[a][b] += 1
        degree[a] += 1
        degree[b] -= 1

    next_gift = {}
    for i in range(len_friends):
        next_gift[i] = 0
    for i in range(len_friends):
        for j in range(i + 1, len_friends):
            if (given_infos[i][j] == 0 and given_infos[j][i] == 0) or given_infos[i][j] == given_infos[j][i]:
                if degree[i] > degree[j]:
                    next_gift[i] += 1
                elif degree[i] < degree[j]:
                    next_gift[j] += 1
            else:
                if given_infos[i][j] > given_infos[j][i]:
                    next_gift[i] += 1
                else:
                    next_gift[j] += 1

    return max(next_gift.values())