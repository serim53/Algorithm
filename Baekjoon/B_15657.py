def dfs(start):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n):
            arr.append(nums[i])
            dfs(i)
            arr.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = []
dfs(0)