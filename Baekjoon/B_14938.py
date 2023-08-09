import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for dest, dist in graph[now]:
            cost = d + dist
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

# n : 지역의 개수, m : 수색범위, r : 길의 개수
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

result = 0
for i in range(1, n + 1):
    distance = [1e9] * (n + 1)
    dijkstra(i)
    temp = 0
    for j in range(1, n + 1):
        if distance[j] <= m:
            temp += items[j]
    result = max(result, temp)

print(result)
