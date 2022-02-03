def solution(brown, yellow):
    answer = []

    x = []
    for i in range(brown):
        if i * i - (brown * 1/2 + 2) * i + brown + yellow == 0:
            x.append(i)

    for i in range(len(x)):
        if x[i] >= (- x[i] + brown * 1/2 + 2):
            answer.append(x[i])
            answer.append(int(- x[i] + brown * 1/2 + 2))

    return answer