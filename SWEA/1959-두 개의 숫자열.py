t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n == m:
        max_value = 0
        for i in range(n):
            max_value += a[i] * b[i]
    else:
        if n > m:
            sums = [0] * (n - m + 1)
            for i in range(len(sums)):
                for j in range(-1, -m - 1, -1):
                    sums[i] += a[j - i] * b[j]
        else:
            sums = [0] * (m - n + 1)
            for i in range(len(sums)):
                for j in range(-1, -n - 1, -1):
                    sums[i] += a[j] * b[j - i]
        sums.sort()
        max_value = sums[-1]

    print("#{} {}".format(t, max_value))