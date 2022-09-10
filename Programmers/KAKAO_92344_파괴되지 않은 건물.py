def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if type == 2 else -degree
        temp[r1][c2 + 1] += -degree if type == 2 else degree
        temp[r2 + 1][c1] += -degree if type == 2 else degree
        temp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    # 행 기준 누적합
    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]
    # 열 기준 누적합
    for j in range(len(temp[0]) - 1):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0: answer += 1
    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))