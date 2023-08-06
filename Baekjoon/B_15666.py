from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []
result = set(result)
for case in combinations_with_replacement(arr, m):
    if case not in result:
        result.add(case)
        print(' '.join(map(str, case)))