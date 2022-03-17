import sys
from collections import deque
input = sys.stdin.readline

def change(dir):
    if dir == "L":
        if direction == [1, 0]:
            return [0, 1]
        elif direction == [-1, 0]:
            return [0, -1]
        elif direction == [0, 1]:
            return [-1, 0]
        elif direction == [0, -1]:
            return [1, 0]
    elif dir == "D":
        if direction == [1, 0]:
            return [0, -1]
        elif direction == [-1, 0]:
            return [0, 1]
        elif direction == [0, 1]:
            return [1, 0]
        elif direction == [0, -1]:
            return [-1, 0]

def check(x, y):
    if [x, y] in q:
        return False
    return True

n = int(input())
s = [[0] * (n + 1) for i in range(n + 1)]
k = int(input())

for i in range(k):
    a, b = map(int, input().split())
    s[a][b] = 1

l = int(input())
d = deque()

for i in range(l):
    a, b = input().split()
    d.append([int(a), b])

direction = [0, 1]
q = deque()
q.append([1, 1])
cnt = 0

while True:
    x, y = q[-1][0], q[-1][1]
    x += direction[0]
    y += direction[1]
    if 0 < x <= n and 0 < y <= n:
        if not check(x, y):
            break
        q.append([x, y])
        if s[x][y] == 1:
            s[x][y] = 0
        else:
            q.popleft()
    else:
        break
    cnt += 1
    if d and cnt == d[0][0]:
        direction = change(d[0][1])
        d.popleft()

print(cnt + 1)