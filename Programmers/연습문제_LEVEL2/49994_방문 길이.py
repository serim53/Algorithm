def solution(dirs):
    d = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
    answer = set()
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x = nx
            y = ny
    return len(answer) // 2