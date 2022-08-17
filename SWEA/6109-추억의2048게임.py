from collections import deque

test_case = int(input())
for tc in range(1, test_case + 1):
    _n, s = input().split()
    nums = [list(map(int, input().split())) for _ in range(int(_n))]
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    result = []
    if s == "up" or s == "down":
        nums = list(zip(*nums))
    elif s == "right":
        for idx, row in enumerate(nums):
            nums[idx] = row[::-1]
    for num in nums:
        line = []
        not_zero = deque()
        for n in num:
            if n != 0:
                not_zero.append(n)
        if s == "down":
            not_zero.reverse()
        while not_zero:
            current = not_zero.popleft()
            if not not_zero:
                line.append(current)
                break
            if current == not_zero[0]:
                not_zero.popleft()
                line.append(current * 2)
            else:
                line.append(current)
        if s == "down" or s == "right":
            line.reverse()
        for _ in range(int(_n) - len(line)):
            if s == "left":
                line.append(0)
            if s == "right":
                line.insert(0, 0)
            if s == "up":
                line.append(0)
            if s == "down":
                line.insert(0, 0)
        result.append(line)
    if s == "up" or s == "down":
        result = list(zip(*result))
    print("#{}".format(tc))
    for r in result:
        for i in range(len(r)):
            print(r[i], end=' ')
        print()
