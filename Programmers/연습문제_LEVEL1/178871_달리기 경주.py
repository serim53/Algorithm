def solution(players, callings):
    info = {}
    for i in range(len(players)):
        info[players[i]] = i
    for name in callings:
        num = info[name]
        info[name] -= 1
        info[players[num - 1]] += 1
        players[num - 1], players[num] = players[num], players[num - 1]
    return players