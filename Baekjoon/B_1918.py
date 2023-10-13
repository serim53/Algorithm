stack = []
exp = input()
for i in exp:
    if i == "(":
        stack.append(i)
    elif i == "+" or i == "-":
        while stack and stack[-1] != "(":
            print(stack.pop(), end="")
        stack.append(i)
    elif i == "*" or i == "/":
        while stack and stack[-1] in ["*", "/"]:
            print(stack.pop(), end="")
        stack.append(i)
    elif i == ")":
        while stack[-1] != "(":
            print(stack.pop(), end="")
        stack.pop()
    elif "A" <= i <= "Z":
        print(i, end="")

if stack:
    for i in range(len(stack)):
        print(stack.pop(), end="")