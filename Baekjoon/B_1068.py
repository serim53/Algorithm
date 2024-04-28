from collections import defaultdict, deque

def remove_root(root):
    q = deque()
    q.append(root)
    while q:
        now = q.popleft()
        for node in tree[now]:
            if node in tree.keys():
                q.append(node)
        tree.pop(now)

n = int(input())
tree = defaultdict(list)
infos = list(map(int, input().split()))
remove_num = int(input())
for i in range(len(infos)):
    if infos[i] != -1:
        tree[infos[i]].append(i)

# 지워야 할 노드에 대한 정보 모두 삭제
if remove_num in tree.keys():
    remove_root(remove_num)

# values가 list 형태로 저장되어 있기 때문에, 하나씩 빼서 values 리스트에 저장
values = []
for v in tree.values():
    for num in v:
        if num != remove_num:
            values.append(num)

result = 0
for i in range(n):
    # 루트 노드가 아니며, 트리 상에 현재 존재할 경우
    if i not in tree.keys() and i in values:
        result += 1
    # 루트 노드이지만, 하위 노드가 지워야 할 노드 한 개인 경우 (삭제 후 리프노드가 됨)
    if i in tree.keys():
        if tree[i] == [remove_num]:
            result += 1
print(result)