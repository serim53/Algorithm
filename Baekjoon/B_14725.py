def add(dic, arr):
    if len(arr) == 0:
        return
    if arr[0] not in dic:
        dic[arr[0]] = {}
    add(dic[arr[0]], arr[1:])

def printTree(dic, length):
    for i in sorted(dic.keys()):
        print('--' * length + i)
        printTree(dic[i], length + 1)

n = int(input())
names = [list(map(str, input().split())) for _ in range(n)]
dic = {}
for name in names:
    add(dic, name[1:])
printTree(dic, 0)