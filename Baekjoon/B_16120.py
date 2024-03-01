def check(input_str):
    stack = []
    flag = False
    for str in input_str:
        # if str == 'A' and (len(stack) < 2 or stack[-2:] != ['P', 'P']):
        #     return flag
        stack.append(str)
        if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(3):
                stack.pop()
    if len(stack) == 1 and stack[0] == 'P':
        flag = True
    return flag

input_str = list(input())
if check(input_str):
    print('PPAP')
else:
    print('NP')