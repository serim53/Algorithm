for tc in range(1, 11):
    n = int(input())
    tree = [list(input().split()) for _ in range(n)]
    result = 1
    for i in range(len(tree)):
        if len(tree[i]) == 2:
            if not tree[i][1].isdigit():
                result = 0
                break
        elif len(tree[i]) == 4:
            if tree[i][1].isdigit():
                result = 0
                break
    print("#{} {}".format(tc, result))
