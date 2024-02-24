s = list(input().rstrip())
t = list(input().rstrip())

flag = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)