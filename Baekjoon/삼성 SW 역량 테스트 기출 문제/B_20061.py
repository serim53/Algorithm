import sys
from collections import deque
input = sys.stdin.readline

blocks = deque()
# 블록을 놓은 횟수
n = int(input())
# 블록
for _ in range(n):
    blocks.append(list(map(int, input().split())))
# 현재 보드에 올라와있는 블록
on_block = deque
green_block = deque
blue_block = deque

while blocks:
    # 빨간색 보드에 블록 올리기
    t, x, y = blocks.popleft()
    if t == 1:
        on_block.append([x, y])
    elif t == 2:
        on_block.append([x, y])
        on_block.append([x, y + 1])
    else:
        on_block.append([x, y])
        on_block.append([x + 1, y])


while on_block:
    x, y = on_block.popleft()
    # 초록색 보드로 블록 이동
    green_x = x + 1
    if 0 <= green_x <= 9:



    # 파란색 보드로 블록 이동

print(on_block)