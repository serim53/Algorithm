def solution(friends, gifts):
    answer = 0
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
        for j in range(len_friends):
            if i == j:
                continue
            if given_infos[i][j] == 0 and given_infos[j][i] == 0:


    return answer

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))