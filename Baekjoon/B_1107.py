import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m:
    broken = list(map(int, input().split()))
else:
    broken = []
result = abs(n - 100)
for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) in broken:
            break
        elif i == len(num) - 1:
            result = min(result, abs(int(num) - n) + len(num))
print(result)