def dfs(n):
    if n in dict:
        return dict[n]
    else:
        dict[n] = dfs(n // p) + dfs(n // q)
        return dict[n]

n, p, q = map(int, input().split())
dict = {}
dict[0] = 1
print(dfs(n))