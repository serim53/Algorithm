from itertools import permutations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []
result = set(result)
for case in permutations(arr, m):
    if case not in result:
        result.add(case)
        print(' '.join(map(str, case)))