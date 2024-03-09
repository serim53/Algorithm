import sys
input = sys.stdin.readline
n = int(input())
towers = list(map(int, input().split()))
result = [0] * n
stack = []
for i in range(len(towers)):
    while stack:
        if towers[stack[-1][0]] < towers[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0] + 1
            break
    stack.append((i, towers[i]))
print(*result)