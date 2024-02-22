def dfs(n, idx, num):
    if idx == N:
        ans = eval(num.replace(' ', ''))
        if ans == 0:
            arr.append(num)
        return
    else:
        n_idx = idx + 1
        dfs(n, n_idx, num + ' ' + str(n_idx))
        dfs(n, n_idx, num + '+' + str(n_idx))
        dfs(n, n_idx, num + '-' + str(n_idx))

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    dfs(N, 1, '1')
    for a in arr:
        print(a)
    print()