for tc in range(1, 11):
    n = int(input())
    tree = [[0]]
    for _ in range(n):
        tree.append(list(input().split()))
    for i in range(len(tree) - 1, 0, -1):
        if len(tree[i]) == 4:
            left = int(tree[int(tree[i][2])][1])
            right = int(tree[int(tree[i][3])][1])
            if tree[i][1] == '-':
                tree[i] = (i, left - right)
            elif tree[i][1] == '+':
                tree[i] = (i, left + right)
            elif tree[i][1] == '*':
                tree[i] = (i, left * right)
            else:
                tree[i] = (i, left / right)
    print("#{} {}".format(tc, int(tree[1][1])))
