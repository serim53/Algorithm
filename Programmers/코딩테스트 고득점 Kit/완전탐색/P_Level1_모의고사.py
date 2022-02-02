def solution(answers):

    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    right = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == st1[i % len(st1)]:
            right[0] += 1
        if answers[i] == st2[i % len(st2)]:
            right[1] += 1
        if answers[i] == st3[i % len(st3)]:
            right[2] += 1

    res = []
    for i in range(len(right)):
        if right[i] == max(right):
            res.append(i + 1)


    return sorted(res)