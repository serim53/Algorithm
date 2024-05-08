def solution(s):
    answer = True
    stack = []
    for str in s:
        if str == '(':
            stack.append(str)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True