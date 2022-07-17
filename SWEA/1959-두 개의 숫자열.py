t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_value = 0

    if n > m:
        for i in range(n - m + 1):
            result = 0
            for j in range(m):
                result += b[j] * a[i + j]
            if result > max_value:
                max_value = result
    else:
        for i in range(m - n + 1):
            result = 0
            for j in range(n):
                result += a[j] * b[i + j]
            if result > max_value:
                max_value = result

    print("#{} {}".format(test_case, max_value))