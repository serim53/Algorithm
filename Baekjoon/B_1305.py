l = int(input())
infos = list(input())
info_len = len(infos)
table = [0 for _ in range(len(infos))]
j = 0
for i in range(1, info_len):
    while j > 0 and infos[i] != infos[j]:
        j = table[j - 1]
    if infos[i] == infos[j]:
        j += 1
        table[i] = j
print(info_len - table[info_len - 1])