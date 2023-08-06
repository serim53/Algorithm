def inorder(v):
    if v <= n:
        inorder(v * 2)
        print(tree[v], end='')
        inorder(v * 2 + 1)

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n + 1)
    for i in range(n):
        nums = list(input().split())
        tree[int(nums[0])] = nums[1]
    print("#{} ".format(tc), end='')
    inorder(1)
    print()