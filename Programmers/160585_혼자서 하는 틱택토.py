def solution(board):
    num_o = 0
    num_x = 0
    temp = ""
    bingo_x = 0
    bingo_o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                num_o += 1
            elif board[i][j] == "X":
                num_x += 1

    if num_x > num_o: return 0

    if (num_o + num_x) % 2 == 0 and num_o != num_x: return 0
    if (num_o + num_x) % 2 == 1 and num_x > num_o: return 0

    if board[0][0] != "." and (board[0][0] == board[1][1] == board[2][2]):
        if board[0][0] == "O":
            bingo_o += 1
            if num_x != num_o - 1: return 0
        elif board[0][0] == "X":
            bingo_x += 1
            if num_x != num_o: return 0
    if board[2][0] != "." and (board[0][2] == board[1][1] == board[2][0]):
        if board[2][0] == "O":
            bingo_o += 1
            if num_x != num_o - 1: return 0
        elif board[2][0] == "X":
            bingo_x += 1
            if num_x != num_o: return 0

    for i in range(3):
        if board[i][0] != "." and board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                bingo_x += 1
                if temp != "O": temp = "X"
            elif board[i][0] == "O":
                bingo_o += 1
                temp = "O"
        if board[0][i] != "." and board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                bingo_x += 1
                if temp != "O": temp = "X"
            elif board[0][i] == "O":
                bingo_o += 1
                temp = "O"

    if bingo_o >= 1 and bingo_x >= 1: return 0

    if temp == "O" and num_x != num_o - 1:
        return 0
    elif temp == "X" and num_x != num_o:
        return 0

    return 1