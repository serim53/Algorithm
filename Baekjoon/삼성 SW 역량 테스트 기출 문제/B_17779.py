n = int(input())
total = 0
result = int(1e9)

a = [[0 for _ in range(n + 1)]]
for i in range(n):
    data = [0] + list(map(int, input().split()))
    total += sum(data)
    a.append(data)

def solve(x, y, d1, d2):
    global result
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    people = [0, 0, 0, 0, 0]
    graph[x][y] = 5
    for i in range(1, d1 + 1):
        graph[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        graph[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        graph[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        graph[x + d2 + i][y + d2 - i] = 5

    # 1
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if graph[i][j] == 5:
                break
            people[0] += a[i][j]

    # 2
    for i in range(1, x + d2 + 1):
        for j in range(n, y, -1):
            if graph[i][j] == 5:
                break
            people[1] += a[i][j]

    # 3
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if graph[i][j] == 5:
                break
            people[2] += a[i][j]

    # 4
    for i in range(x + d2 + 1, n + 1):
        for j in range(n, y - d1 + d2 - 1, -1):
            if graph[i][j] == 5:
                break
            people[3] += a[i][j]

    people[4] = total - sum(people[0:4])
    result = min(result, max(people) - min(people))


for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if x + d1 + d2 > n or y - d1 < 1 or y + d2 > n:
                    continue
                solve(x, y, d1, d2)

print(result)
