a, b = map(int, input().split())
if a < b:
    a, b = b, a
while b != 0:
    a = a % b
    a, b = b, a

print("1" * a)