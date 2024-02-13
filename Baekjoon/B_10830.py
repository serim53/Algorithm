import sys
input = sys.stdin.readline

def multi(mat1, mat2):
    res_mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res_mat[i][j] += mat1[i][k] * mat2[k][j] % 1000
    return res_mat

def square(matrix, n):
    if n == 1:
        return matrix
    temp = square(matrix, n // 2)
    if n % 2 == 0 :
        return multi(temp, temp)
    else :
        return multi(multi(temp, temp), matrix)

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = square(a, b)
for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()