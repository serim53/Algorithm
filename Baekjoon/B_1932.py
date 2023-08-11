# dfs : 시간 초과
# def dfs(x, y, cnt):
#     global result
#     if x == n - 1:
#         result = max(result, cnt)
#         return
#     if y >= 0:
#         visited[x + 1][y] = 1
#         dfs(x + 1, y, cnt + arr[x + 1][y])
#         visited[x + 1][y] = 0
#     if y + 1 <= x:
#         visited[x + 1][y + 1] = 1
#         dfs(x + 1, y + 1, cnt + arr[x + 1][y + 1])
#         visited[x + 1][y + 1] = 0
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# result = 0
# visited[0][0] = 1
# dfs(0, 0, arr[0][0])
# print(result)

# dp
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif j == i:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

print(max(arr[n - 1]))