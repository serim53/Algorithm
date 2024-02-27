n = int(input())
result = 0
while n % 5 != 0 and n >= 3:
    n -= 3
    result += 1
if n % 5 == 0:
    result += n // 5
else:
    result = -1
print(result)