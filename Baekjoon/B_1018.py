n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
count = []

for a in range(n - 7):
    for b in range(m - 7):
        numW = 0
        numB = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        numW += 1
                    if board[i][j] != 'B':
                        numB += 1
                else:
                    if board[i][j] != 'B':
                        numW += 1
                    if board[i][j] != 'W':
                        numB += 1
        count.append(min(numW, numB))
print(min(count))