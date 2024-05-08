def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    num_remove = []
    for i in reserve:
        if i in lost:
            num_remove.append(i)

    for num in num_remove:
        lost.remove(num)
        reserve.remove(num)

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)