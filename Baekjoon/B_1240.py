from collections import deque
import sys
input = sys.stdin.readline

def get_distance(s, e):
    if distance[s][e] != 1e9:
        return distance[s][e]
    q = deque() # 현재 노드, 거리
    q.append([s, 0])
    visited[s] = 1
    while q:
        node, dist = q.popleft()
        if node == e:
            return dist
        for n in graph[node]:
            if not visited[n]:
                visited[n] = 1
                q.append([n, dist + distance[node][n]])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    distance[a][b] = d
    distance[b][a] = d
for _ in range(m):
    visited = [0] * (n + 1)
    s, e = map(int, input().split())
    print(get_distance(s, e))