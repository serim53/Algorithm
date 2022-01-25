n, k = map(int, input().split())

ar = [i for i in range(1, n + 1)]
index = 0
res = []

for _ in range(n):
    index += k - 1
    if index >= len(ar):
        index = index % len(ar)
    res.append(str(ar.pop(index)))

print("<",", ".join(res)[:],">", sep='')