T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            row_num[arr[i][j]] += 1
            col_num[arr[j][i]] += 1

        for k in range(1, 10):
            if row_num[k] != 1:
                result = 0
                break
            if col_num[k] != 1:
                result = 0
                break

    for i in range(3):
        for j in range(3):
            square_num = [0] * 10
            for k in range(3):
                for l in range(3):
                    square_num[arr[3 * i + k][3 * j + l]] += 1

            for k in range(1, 10):
                if square_num[k] != 1:
                    result = 0
                    break

    print('#{} {}'.format(test_case, result))