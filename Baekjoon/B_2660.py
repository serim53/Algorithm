from collections import deque, defaultdict

def get_score(i):
    visited = [0] * (n + 1)
    visited[i] = 1
    q = deque()
    q.append([i, 0])
    score = 0
    while q:
        now, num = q.popleft()
        score = num
        for ad in relation[now]:
            if not visited[ad]:
                q.append([ad, num + 1])
                visited[ad] = 1
    return score

n = int(input())
relation = defaultdict(list)
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    relation[a].append(b)
    relation[b].append(a)
scores = []
for i in range(1, n + 1):
    scores.append(get_score(i))
min_score = min(scores)
candidate = []
for i in range(len(scores)):
    if scores[i] == min_score:
        candidate.append(i + 1)
print(min_score, len(candidate))
print(*candidate)