for _ in range(10):
    tc, length = map(int, input().split())
    road = list(map(int, input().split()))
    adj = [[] for _ in range(100)]
    for i in range(length):
        adj[road[i * 2]].append(road[i * 2 + 1])
    visited = [False] * 100
    stack = [0]
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            for a in adj[now]:
                if not visited[a]:
                    stack.append(a)
    print("#{} {}".format(tc, 1 if visited[99] else 0))
