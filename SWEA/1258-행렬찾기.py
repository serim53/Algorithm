def find_row(i, j):
    row_len = 0
    while 0 <= i < n and matrix[i][j] > 0:
        i += 1
        row_len += 1
    return row_len
def find_col(i, j):
    col_len = 0
    while 0 <= j < n and matrix[i][j] > 0:
        j += 1
        col_len += 1
    return col_len
def change_zero(i, j, row_len, col_len):
    for row in range(i, i + row_len):
        for col in range(j, j + col_len):
            matrix[row][col] = 0
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                col_len = find_col(i, j)
                row_len = find_row(i, j)
                result.append((row_len, col_len, row_len * col_len))
                change_zero(i, j, row_len, col_len)
                result.sort(key=lambda x: (x[2], x[0]))
    print("#{} {}".format(tc, len(result)), end=' ')
    for i in result:
        print(i[0], i[1], end=' ')
    print()