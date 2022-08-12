for tc in range(1, 11):
    length = int(input())
    exp = list(map(str, input()))
    postfix = []
    stack = []
    stack_cal = []
    prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    for e in exp:
        if e.isdigit():
            postfix.append(e)
        elif e == '(':
            stack.append(e)
        elif e == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and prior[e] <= prior[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(e)
    while len(stack) != 0:
        postfix.append(stack.pop())

    for p in postfix:
        if p.isdigit():
            stack_cal.append(int(p))
        elif p == '+':
            a = stack_cal.pop()
            b = stack_cal.pop()
            stack_cal.append(a + b)
        elif p == '-':
            a = stack_cal.pop()
            b = stack_cal.pop()
            stack_cal.append(a - b)
        elif p == '*':
            a = stack_cal.pop()
            b = stack_cal.pop()
            stack_cal.append(a * b)
        elif p == '/':
            a = stack_cal.pop()
            b = stack_cal.pop()
            stack_cal.append(a / b)
    print("#{} {}".format(tc, stack_cal.pop()))
