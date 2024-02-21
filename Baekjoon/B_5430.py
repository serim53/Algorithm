from collections import deque

def execute(cmds, nums):
    rev = 0
    for cmd in cmds:
        if cmd == 'D':
            if not len(nums):
                return 'error'
            if rev % 2 == 0:
                nums.popleft()
            else:
                nums.pop()
        else:
            rev += 1
    if rev % 2 == 1:
        nums.reverse()
    return "[" + ",".join(nums) + "]"

t = int(input())
for _ in range(t):
    cmds = input().rstrip()
    n = int(input())
    nums = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        nums = deque()
    print(execute(cmds, nums))