s = input()
slist = list(s)
list = [-1 for i in range(26)]

for i in range(len(slist)):
    index = ord(slist[i]) - 97
    if list[index] == -1:
        list[index] = i

for i in range(26):
    print(list[i], end=' ')