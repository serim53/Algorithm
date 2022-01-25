t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    mul = a * b
    while b != 0:
        a = a % b
        a, b = b, a
    print(int(mul / a))