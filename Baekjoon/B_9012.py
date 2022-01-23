T = int(input())
for i in range(T):
    st = input()
    stlist = list(st)
    sum = 0
    for i in stlist:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')