from collections import defaultdict
# n: 회원 수, w: 역기 무게, m: 친분 관계
n, m = map(int, input().split())
w = list(map(int, input().split()))
result = 0
dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
for i in range(1, n + 1):
    weight = w[i - 1]
    flag = True
    for member in dic[i]:
        if w[member - 1] >= weight:
            flag = False
            break
    if flag:
        result += 1
print(result)
