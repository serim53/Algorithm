import sys
sys.stdin = open("input.txt", "r")

def find_parent(node, parent):
    if tree[node][2]:
        parent.append(tree[node][2])
        find_parent(tree[node][2], parent)

def find_common_parent(parent1, parent2):
    for p1 in parent1:
        for p2 in parent2:
            if p1 == p2:
                return p2

def find_subtree(n):
    global size
    for i in range(2):
        if tree[n][i]:
            size += 1
            find_subtree(tree[n][i])


t = int(input())
for tc in range(1, t + 1):
    v, e, n, m = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(v + 1)]
    size = 1
    for i in range(e):
        if tree[edges[i * 2]][0]:
            tree[edges[i * 2]][1] = edges[i * 2 + 1]
        else:
            tree[edges[i * 2]][0] = edges[i * 2 + 1]
        tree[edges[i * 2 + 1]][2] = edges[i * 2]

    parent_n, parent_m = [], []
    find_parent(n, parent_n)
    find_parent(m, parent_m)

    common_parent = find_common_parent(parent_n, parent_m)
    find_subtree(common_parent)

    print("#{} {} {}".format(tc, common_parent, size))