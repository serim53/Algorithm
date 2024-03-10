n = int(input())
stack = []
result = []
flag = True
idx = 1
for i in range(n):
    num = int(input())
    while idx <= num:
        stack.append(idx)
        result.append("+")
        idx += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break
if flag:
    for i in result:
        print(i)
else:
    print("NO")