n, m = map(int, input().split())
dict = {}

for idx in range(1, n + 1):
    name = input().rstrip()
    dict[idx] = name
    dict[name] = idx

for _ in range(m):
    ipt = input().rstrip()
    if ipt.isdigit():
        print(dict[int(ipt)])
    else:
        print(dict[ipt])