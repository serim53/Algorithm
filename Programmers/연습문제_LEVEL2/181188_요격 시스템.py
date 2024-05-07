def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])

    temp = 0
    for target in targets:
        if target[0] >= temp:
            answer += 1
            temp = target[1]

    return answer