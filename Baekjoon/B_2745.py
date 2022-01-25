N, B = input().split()

N = N[::-1]
B = int(B)

table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

for i in range(len(N)):
    result += table.index(N[i]) * (B ** i)

print(result)