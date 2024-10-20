from collections import deque

def solution(x, y, n):
    q = deque([(y, 0)])
    while q:
        num, cnt = q.popleft()
        if num == x:
            return cnt
        if num - n >= x:
            q.append((num - n, cnt + 1))
        if num % 2 == 0:
            q.append((num // 2, cnt + 1))
        if num % 3 == 0:
            q.append((num // 3, cnt + 1))
    return -1
