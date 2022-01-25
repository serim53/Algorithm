N, B = map(int, input().split())
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
while N != 0:
    result += table[N % B]
    N //= B
print(result[::-1])