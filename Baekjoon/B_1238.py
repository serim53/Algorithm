import heapq


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance = [1e9] * (n + 1)
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    return distance[end]


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

result = 0
for i in range(1, n + 1):
    if i == x:
        continue
    result = max(result, dijkstra(i, x) + dijkstra(x, i))

print(result)
