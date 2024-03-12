n = int(input())
nums = list(map(int, input().split()))
stack = []
result = []
for i in range(n - 1, -1, -1):
    num = nums[i]
    while stack and stack[-1] <= num:
        stack.pop()
    if not stack:
        result.append(-1)
    else:
        result.append(stack[-1])
    stack.append(num)
print(' '.join(str(result[i]) for i in range(n - 1, -1, -1)))