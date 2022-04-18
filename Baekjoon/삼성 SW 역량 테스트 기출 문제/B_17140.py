from collections import Counter
from functools import reduce


def rc(array):
    maxList = 0
    for i in range(len(array)):
        X = Counter(array[i])
        del X[0]
        X = list(X.items())
        X.sort(key=lambda x: (x[1], x[0]))
        if len(X) > 50: X = X[:50]
        array[i] = reduce(lambda x, y: list(x) + list(y), X[1:], list(X[0]))
        maxList = max(maxList, len(array[i]))

    for i in range(len(array)):
        if len(array[i]) < maxList:
            array[i].extend([0] * (maxList - len(array[i])))


def main():
    r, c, k = map(int, input().split())
    r, c = r - 1, c - 1
    a = [list(map(int, input().split())) for _ in range(3)]
    time = 0
    if r < len(a) and c < len(a[0]):
        if a[r][c] == k: return time

    while True:
        if len(a) >= len(a[0]):
            rc(a)
        else:
            a = list(map(list, zip(*a)))
            rc(a)
            a = list(map(list, zip(*a)))
        time += 1
        if time > 100: return -1
        if r < len(a) and c < len(a[0]):
            if a[r][c] == k: return time


print(main())
