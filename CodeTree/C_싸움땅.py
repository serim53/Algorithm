def fight(x, y, winner, loser, power_diff):
    # 승자는 힘 차이만큼 포인트 얻음
    score[winner - 1] += power_diff
    # 승자는 해당 위치에 그대로 남음
    user_info[winner] = [x, y]
    user_graph[x][y] = winner
    # 패자는 총 내려놓고 가던 방향으로 한 칸 이동
    if loser in user_gun.keys():
        graph[x][y].append(user_gun[loser])
        user_gun.pop(loser)
    # 패자의 방향
    dir = direction[loser]
    nx, ny = x + dx[dir], y + dy[dir]
    # 패자가 이동해야 하는 좌표가 격자를 넘어서거나 다른 플레이어가 있을 경우
    while 0 > nx or nx >= n or 0 > ny or ny >= n or user_graph[nx][ny]:
        # 시계방향으로 90도 회전
        dir = (dir + 1) % 4
        direction[loser] = dir
        nx, ny = x + dx[dir], y + dy[dir]
    # 패자 이동
    user_graph[nx][ny] = loser
    user_info[loser] = [nx, ny]
    # 패자가 이동한 위치에 총이 있을 경우
    if graph[nx][ny]:
        # 가장 공격력 높은 총을 가짐
        max_loser_gun = max(graph[nx][ny])
        user_gun[loser] = max_loser_gun
        graph[nx][ny].remove(max_loser_gun)
    # 승자의 위치에 총이 있을 경우
    if graph[x][y]:
        # 가장 공격력 높은 총
        max_winner_gun = max(graph[x][y])
        # 승자가 이미 총을 가지고 있을 경우
        if winner in user_gun.keys():
            users = user_gun[winner]
            # 승자의 것보다 총이 더 셀 경우 가지고 있던 것을 내려놓고 더 센 총을 가져감
            if max_winner_gun > users:
                graph[x][y].append(users)
                user_gun[winner] = max_winner_gun
                graph[x][y].remove(max_winner_gun)
        # 승자가 총을 가지고 있지 않을 경우
        else:
            user_gun[winner] = max_winner_gun
            graph[x][y].remove(max_winner_gun)


n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
user_graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] += [temp[j]]
direction = {}
power = {}
user_info = {}
user_gun = {}
result = [0] * m
for i in range(1, m + 1):
    x, y, d, s = map(int, input().split())
    user_graph[x - 1][y - 1] = i
    user_info[i] = [x - 1, y - 1]
    direction[i] = d
    power[i] = s

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

score = [0] * m  # 각 플레이어의 점수

game = 1
while game <= k:
    # 한 플레이어씩 이동
    for player in range(1, m + 1):
        # 현재 플레이어의 위치와 방향
        x, y = user_info[player]
        dir = direction[player]
        nx, ny = x + dx[dir], y + dy[dir]
        # 이동할 좌표가 격자를 벗어날 경우
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            # 반대로 방향을 바꾸어 이동
            direction[player] = (dir + 2) % 4
            dir = direction[player]
            nx, ny = x + dx[dir], y + dy[dir]
        # 이동 전 위치를 비워줌
        user_graph[x][y] = 0
        # 이동할 위치에 플레이어 O
        if user_graph[nx][ny]:
            opponent = user_graph[nx][ny]   # 이동할 위치에 있는 플레이어
            opponent_power = power[opponent]
            if opponent in user_gun.keys():
                opponent_power += user_gun[opponent]
            my_power = power[player]
            if player in user_gun.keys():
                my_power += user_gun[player]
            # 싸움 후 얻을 포인트
            power_diff = abs(my_power - opponent_power)
            # 초기 능력치 + 공격력 같으면
            if my_power == opponent_power:
                # 초기 능력치 큰 플레이어가 이김
                if power[opponent] > power[player]:
                    fight(nx, ny, opponent, player, power_diff)
                else:
                    fight(nx, ny, player, opponent, power_diff)
            # 내 (초기 능력치 + 공격력)이 더 크면
            elif my_power > opponent_power:
                fight(nx, ny, player, opponent, power_diff)
            # 상대방 (초기 능력치 + 공격력)이 더 크면
            else:
                fight(nx, ny, opponent, player, power_diff)
        # 이동할 위치에 플레이어 X
        else:
            if graph[nx][ny]:   # 해당 위치에 총 O
                max_gun = max(graph[nx][ny])
                if player in user_gun.keys():   # 유저가 이미 총을 가지고 있을 경우
                    if user_gun[player] < max_gun:   # 유저꺼가 더 약할 경우
                        graph[nx][ny].append(user_gun[player])
                        user_gun[player] = max_gun
                        graph[nx][ny].remove(max_gun)
                else:   # 유저가 총이 없을 경우
                    user_gun[player] = max_gun
                    graph[nx][ny].remove(max_gun)
            user_graph[nx][ny] = player
            user_graph[x][y] = 0
            user_info[player] = [nx, ny]
    game += 1
print(*score)