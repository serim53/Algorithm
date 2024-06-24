def solution(board, h, w):
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    color = board[h][w]
    n = len(board)
    for d in range(4):
        nx, ny = h + dx[d], w + dy[d]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color:
            answer += 1
    return answer
