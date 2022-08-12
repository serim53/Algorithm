for tc in range(1, 11):
    n, m = input().split()
    nums = list(m)
    stack = list()
    for num in nums:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    print("#{} {}".format(tc, ''.join(stack)))
