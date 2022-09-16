def dfs(idx):
    global temp
    global max_arr
    for j in range(n):
        if visited[j] == 0 and screws_sorted[j][0] == idx:
            visited[j] = 1
            temp.append(screws_sorted[j][0])
            temp.append(screws_sorted[j][1])
            dfs(screws_sorted[j][1])
    if len(max_arr) < len(temp):
        max_arr = temp
    return

t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    inp = list(map(str, input().split()))
    screws = [0 for _ in range(n)]
    for i in range(n):
        screws[i] = [inp[i * 2], inp[i * 2 + 1]]
    screws_sorted = sorted(screws, key=lambda x: x[0])
    max_arr = []
    for screw in range(n):
        visited = [0 for _ in range(n)]
        temp = [screws_sorted[screw][0], screws_sorted[screw][1]]
        visited[screw] = 1
        dfs(screws_sorted[screw][1])
        visited[screw] = 0
    print('#{}'.format(tc), end=' ')
    for r in max_arr:
        print(r, end=' ')
    print()