from collections import defaultdict, deque

def solution(n, edge):
    dict = defaultdict(list)
    for e in edge:
        start, end = e
        dict[start].append(end)
        dict[end].append(start)
    visited = [0] * (n + 1)
    max_len, cnt = 0, 1
    q = deque()
    q.append([1, 0])
    visited[1] = 1
    while q:
        node, l = q.popleft()
        for i in dict[node]:
            if not visited[i]:
                q.append([i, l + 1])
                visited[i] = 1
                if max_len < l + 1:
                    cnt = 1
                    max_len = l + 1
                elif max_len == l + 1:
                    cnt += 1
    return cnt