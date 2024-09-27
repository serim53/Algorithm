def dfs(num, x, y, cnt):
    global answer
    if num == 0:
        answer = cnt
        return
    num_add = 2 ** (num - 1)
    # 1사분면
    if x <= r < x + num_add and y <= c < y + num_add:
        dfs(num - 1, x, y, cnt)
    # 2사분면
    elif x <= r < x + num_add and y + num_add <= c < y + 2 ** num:
        dfs(num - 1, x, y + num_add, cnt + num_add ** 2)
    # 3사분면
    elif x + num_add <= r < x + 2 ** num and y <= c < y + num_add:
        dfs(num - 1, x + num_add, y, cnt + (num_add ** 2) * 2)
    # 4사분면
    else:
        dfs(num - 1, x + num_add, y + num_add, cnt + (num_add ** 2) * 3)
    

n, r, c = map(int, input().split())
answer = 0
if r != 0 or c != 0:
    dfs(n, 0, 0, 0)
print(answer)
