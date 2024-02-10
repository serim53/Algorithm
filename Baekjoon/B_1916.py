from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance[start - 1] = 0
    heappush(q, (0, start - 1))
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for end, weight in graph[now]:
            weight += dist
            if weight < distance[end]:
                distance[end] = weight
                heappush(q, [weight, end])

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
distance = [1e9] * n
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s - 1].append((e - 1, w))
start, end = map(int, input().split())
dijkstra(start)
print(distance[end - 1])