def solution(data, col, row_begin, row_end):
    answer = 0
    len_row = len(data[0])
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin - 1, row_end):
        temp = 0
        for j in range(len_row):
            temp += data[i][j] % (i + 1)
        answer = answer ^ temp
    return answer