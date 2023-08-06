for tc in range(1, 11):
    n = int(input())
    input_list = list(map(str, input()))
    stack = []
    result = 0

    left = ['(', '{', '[', '<']
    right = [')', '}', ']', '>']
    for i in range(n):
        if input_list[i] in left:
            stack.append(input_list[i])
        if input_list[i] in right:
            if right.index(input_list[i]) == left.index(stack[-1]):
                stack.pop()
            else: break
    if len(stack) == 0: result = 1
    print("#{} {}".format(tc, result))