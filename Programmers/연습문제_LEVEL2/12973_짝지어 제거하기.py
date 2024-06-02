def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        if len(stack) >= 2 and stack[-2] == stack[-1]:
            stack = stack[:-2]
    if stack:
        return 0
    else:
        return 1