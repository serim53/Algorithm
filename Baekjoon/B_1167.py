from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    arr = list(map(int, input().split()))
    for e in range(1, len(arr) - 2, 2):
        graph[arr[0]].append((arr[e], arr[e + 1]))


def bfs(start):
    visited = [-1] * (v + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    result = [0, 0]  # 가장 멀리 있는 노드와 거리
    while queue:
        now = queue.popleft()
        for n, e in graph[now]:
            if visited[n] == -1:
                visited[n] = visited[now] + e
                queue.append(n)
                if result[1] < visited[n]:
                    result = n, visited[n]
    return result

# 2번의 bfs
# 1. 첫 번째 노드에서 가장 멀리 떨어진 노드를 찾음
node, _ = bfs(1)
# 2. 해당 노드에서 가장 멀리 있는 노드와의 거리를 찾음
_, distance = bfs(node)

print(distance)