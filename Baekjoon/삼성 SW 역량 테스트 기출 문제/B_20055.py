from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
durability = deque(list(map(int, input().split())))
robot = deque([0]*n)

result = 0

while durability.count(0) < k:
    durability.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and durability[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                durability[i + 1] -= 1
        robot[-1] = 0
    if robot[0] == 0 and durability[0] >= 1:
        robot[0] = 1
        durability[0] -= 1
    result += 1
    if durability.count(0) >= k:
        break

print(result)