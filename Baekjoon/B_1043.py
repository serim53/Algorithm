from collections import deque

# 사람 수 n, 파티 수 m
n, m = map(int, input().split())
# 진실을 아는 사람
know = list(map(int, input().split()))
know.pop(0)
# 각 사람 별 마주친 사람
meet = list({0} for _ in range(n + 1))
party = []

for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(1, temp[0] + 1):
        for j in range(1, temp[0] + 1):
            if i != j:
                meet[temp[i]].add(temp[j])
    party.append(temp)

queue = deque(know)
while queue:
    now = queue.popleft()
    for i in (meet[now]):
        if i in know:
            continue
        else:
            know.append(i)
            queue.append(i)

result = 0
for i in range(m):
    intersection = list(set(know) & set(party[i][1:]))
    if intersection:
        continue
    else:
        result += 1

print(result)