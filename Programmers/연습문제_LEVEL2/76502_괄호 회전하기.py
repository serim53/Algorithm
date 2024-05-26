def solution(s):
    answer = 0
    len_s = len(s)
    for i in range(len_s):
        stack = []
        for j in range(i, len_s + i):
            now = s[j % len_s]
            if stack:
                if stack[-1] == '[' and now == ']':
                    stack.pop()
                elif stack[-1] == '(' and now == ')':
                    stack.pop()
                elif stack[-1] == '{' and now == '}':
                    stack.pop()
                else:
                    stack.append(now)
            else:
                stack.append(now)
        if not stack:
            answer += 1
    return answer