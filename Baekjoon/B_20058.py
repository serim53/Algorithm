import sys
from collections import deque

input = sys.stdin.readline

def check_range(y, x):
    return (0 <= y < 2**N) and (0 <= x < 2**N)

def rotate(n, m, size):
    for y in range(n, n+size):
        idx = n
        for x in range(m, m+size):
            rotated_board[idx][(n+m+size) - (y+1)] = board[y][x]
            idx += 1

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    count = 0
    while q:
        cy, cx = q.popleft()
        count += 1
        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]
            if check_range(ny, nx) and visited[ny][nx] == False and board[ny][nx] > 0:
                q.append((ny, nx))
                visited[ny][nx] = True

    return count

def show(board):
    for y in range(2**N):
        for x in range(2**N):
            print(board[y][x], end=' ')
        print()
    print()

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
cmd = list(map(int, input().split()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for L in cmd:
    rotated_board = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for y in range(0, 2**N - 2**L + 1, 2**L):
        for x in range(0, 2**N - 2**L + 1, 2**L):
            rotate(y, x, 2**L)
    q = deque()
    for y in range(2**N):
        for x in range(2**N):
            if rotated_board[y][x] > 0:
                count = 0
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if check_range(ny, nx) and rotated_board[ny][nx] > 0:
                        count += 1
                if count < 3:
                    q.append((y, x))

    while q:
        y, x = q.popleft()
        rotated_board[y][x] -= 1

    board = rotated_board

total = 0
max_area = 0
visited = [[False for _ in range(2**N)] for _ in range(2**N)]
for y in range(2**N):
    for x in range(2**N):
        if board[y][x] > 0:
            total += board[y][x]
            max_area = max(max_area, bfs(y, x))

print(total)
print(max_area)