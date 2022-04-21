from collections import deque

wheel = [deque(map(int, input())) for _ in range(4)]
q = deque(list(map(int, input().split())) for _ in range(int(input())))

# 2, 6
# N극 0, S극 1

# def move(wheel, dir):
#     if dir == 1:
#         wheel.insert(0, wheel[7])
#         del wheel[7]
#         return wheel
#     else:
#         wheel.append(wheel[0])
#         del wheel[0]
#         return wheel

while q:
    a, b = q.popleft()
    a -= 1
    temp2 = wheel[a][2]
    temp6 = wheel[a][6]
    wheel[a].rotate(b)
    temp_dir = b

    dir = temp_dir
    # 시작 톱니 왼쪽
    for i in range(a - 1, -1, -1):
        if wheel[i][2] != temp6:
            temp6 = wheel[i][6]
            wheel[i].rotate(dir * (-1))
            dir *= -1
        else:
            break
    # 시작 톱니 오른쪽
    dir = temp_dir
    for i in range(a + 1, 4):
        if wheel[i][6] != temp2:
            temp2 = wheel[i][2]
            wheel[i].rotate(dir * (-1))
            dir *= -1
        else:
            break

ans = 0
for i in range(4):
    if wheel[i][0] == 1:
        ans += (2 ** i)

print(ans)