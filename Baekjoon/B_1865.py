def bellmanFord(start):
    distance[start] = 0
    for i in range(1, n + 1):
        for j in range(len(edges)):
            now, next, cost = edges[j]
            if distance[now] + cost < distance[next]:
                distance[next] = distance[now] + cost
                if i == n:
                    return True
    return False

TC = int(input())
for _ in range(TC):
    # n : 지점 수, m : 도로 수, w : 웜홀 수
    n, m, w = map(int, input().split())
    edges = []
    distance = [10001] * (n + 1)
    for _ in range(m):  # 도로
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):  # 웜홀
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    if bellmanFord(1):
        print("YES")
    else:
        print("NO")