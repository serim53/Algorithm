n, k = map(int, input().split())
s = list(map(int, input().split()))
for _ in range(k):
    a, b = map(int, input().split())
    sum = 0
    for i in range(a - 1, b):
        sum += s[i]
    print('{:.2f}'.format(sum / (b - a + 1), 2))
