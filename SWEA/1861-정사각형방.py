def dfs(start):
    global n
    cnt = 0
    stack = [start]
    while stack:
        x, y = stack.pop()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if nums[nx][ny] == nums[x][y] + 1:
                    stack.append((nx, ny))
    return cnt


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    result = [1e9, 0]
    for i in range(n):
        for j in range(n):
            cnt = dfs((i, j))
            if cnt > result[1]:
                result[1] = cnt
                result[0] = nums[i][j]
            elif cnt == result[1]:
                if nums[i][j] < result[0]:
                    result[0] = nums[i][j]

    print("#{} {} {}".format(tc, result[0], result[1]))
