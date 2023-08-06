from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
print(graph[0][1])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
queue = deque()
queue.append([0, 0, 1, False])
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
result = -1
while queue:
    print(queue)
    x, y, distance, broke = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        distance += 1
        if nx == n - 1 and ny == m - 1:
            print("a")
            result = distance
            break
        if 0 <= nx < n - 1 and 0 <= ny < m - 1 and not visited[nx][ny]:
            print(nx, ny)
            if not graph[nx][ny]:
                queue.append([nx, ny, distance, broke])
                visited[nx][ny] = 1
            if graph[nx][ny] and not broke:
                queue.append([nx, ny, distance, True])
                visited[nx][ny] = 1

print(result)
