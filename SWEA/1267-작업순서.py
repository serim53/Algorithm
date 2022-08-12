from collections import deque
for tc in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))  # 간선

    indegree = [0] * (v + 1)   # 진입차수
    graph = [[] for _ in range(v + 1)]  # 연결된 노드

    queue = deque()
    result = []

    for i in range(0, e):
        start = edges[i * 2]
        end = edges[i * 2 + 1]
        graph[start].append(end)
        indegree[end] += 1

    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.pop()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    result = ' '.join(list(map(str, result)))
    print("#{} {}".format(tc, result))
