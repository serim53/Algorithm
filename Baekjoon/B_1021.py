from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])
result = 0
for num in nums:
    while True:
        if q[0] == num:
            q.popleft()
            break
        else:
            if q.index(num) <= len(q) // 2:
                q.rotate(-1)
            else:
                q.rotate(1)
            result += 1
print(result)