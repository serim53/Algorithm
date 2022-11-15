def dfs(height, sum_h):
    global min_diff
    if sum_h >= b:
        if min_diff > sum_h - b:
            min_diff = sum_h - b
        return
    if len(height) == 0:
        return
    num = height.pop(0)
    # 현재 인덱스 값을 추가
    dfs(height[:], sum_h + num)
    # 현재 인덱스 값을 추가 X
    dfs(height[:], sum_h)

t = int(input())
for tc in range(1, t + 1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    min_diff = 1e9
    dfs(height, 0)

    print("#{} {}".format(tc, min_diff))