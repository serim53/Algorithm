s = input()
slist = list(s)
list = [0 for i in range(26)]

for i in slist:
    index = ord(i) - 97
    list[index] += 1

for i in range(26):
    print(list[i], end=' ')