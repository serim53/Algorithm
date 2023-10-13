def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n)]
result = 0
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find:
        print(i + 1)
        break
    union(find(a), find)
else:
    print(0)