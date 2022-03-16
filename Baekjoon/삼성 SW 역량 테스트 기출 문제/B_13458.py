import sys, math
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = n

for i in a:
    i -= b
    if i > 0:
        result += math.ceil(i / c)

print(result)