import heapq, sys
input = sys.stdin.readline

def dijkstra(start, end):
    distance = [1e9] * (n + 1)
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, weight in graph[now]:
            weight += dist
            if weight < distance[node]:
                distance[node] = weight
                heapq.heappush(q, (weight, node))
    return distance[end]


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))
route1, route2 = map(int, input().split())
path1 = dijkstra(1, route1) + dijkstra(route1, route2) + dijkstra(route2, n)
path2 = dijkstra(1, route2) + dijkstra(route2, route1) + dijkstra(route1, n)
path3 = 1e9
if (route1 == 1 and route2 == n) or (route1 == n and route2 == 1):
    path3 = dijkstra(1, n)

result = min(path1, path2, path3)
print(result if result < 1e9 else -1)