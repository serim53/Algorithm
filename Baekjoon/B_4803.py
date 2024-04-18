from collections import deque

def find_cycle(start):
    flag = False
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if visited[now]:
            flag = True
        visited[now] = 1
        for node in graph[now]:
            if node == now:
                flag = True
            if not visited[node]:
                q.append(node)
    return flag

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    result = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n + 1):
        if not visited[i]:
            if not find_cycle(i):
                result += 1
    if result == 0:
        print("Case {}: No trees.".format(case))
    elif result == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, result))
    case += 1