def solution(k, score):
    answer = []
    temp = []
    for s in score:
        temp.append(s)
        temp.sort(reverse=True)
        if len(temp) < k:
            answer.append(temp[len(temp) - 1])
        else:
            answer.append(temp[k - 1])
    return answer