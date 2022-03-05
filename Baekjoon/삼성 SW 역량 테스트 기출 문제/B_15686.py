from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
result = 9999

for r in range(n):
    for c in range(n):
        if data[r][c] == 1:
            house.append((r, c))    # 일반 집
        elif data[r][c] == 2:
            chicken.append((r, c))    # 치킨집

for c in combinations(chicken, m):
    temp = 0
    for h in house:
        chicken_len = 9999
        for i in range(m):
            chicken_len = min(chicken_len, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        temp += chicken_len
    result = min(result, temp)

print(result)