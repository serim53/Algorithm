def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    for arr in photo:
        score = 0
        for n in arr:
            if n in dict.keys():
                score += dict[n]
        answer.append(score)
    return answer