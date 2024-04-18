import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def get_count(root):
    count[root] = 1
    for node in graph[root]:
        if not count[node]:
            get_count(node)
            count[root] += count[node]


# n : 정점 수, r : 루트 번호, q : 쿼리 수
n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = [0] * (n + 1)
get_count(r)

for _ in range(q):
    u = int(input())
    print(count[u])