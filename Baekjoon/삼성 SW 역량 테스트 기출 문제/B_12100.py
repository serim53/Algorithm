from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def move(graph, d):
    if d == 0:    # 동쪽
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][top] == 0:
                        graph[i][top] = temp
                    elif graph[i][top] == temp:
                        graph[i][top] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        graph[i][top] = temp
    elif d == 1:    # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][top] == 0:
                        graph[i][top] = temp
                    elif graph[i][top] == temp:
                        graph[i][top] = temp * 2
                        top += 1
                    else:
                        top += 1
                        graph[i][top] = temp
    elif d == 2:    # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[top][j] == 0:
                        graph[top][j] = temp
                    elif graph[top][j] == temp:
                        graph[top][j] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        graph[top][j] = temp
    elif d == 3:    # 북쪽
        for j in range(n):
            top = 0
            for i in range(1, n):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[top][j] == 0:
                        graph[top][j] = temp
                    elif graph[top][j] == temp:
                        graph[top][j] = temp * 2
                        top += 1
                    else:
                        top += 1
                        graph[top][j] = temp
    return graph


def dfs(graph, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, graph[i][j])
        return

    for i in range(4):
        temp_board = move(deepcopy(graph), i)
        dfs(temp_board, cnt + 1)

ans = 0
dfs(graph, 0)
print(ans)

