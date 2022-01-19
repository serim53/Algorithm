import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    [x, y] = list(map(int, input().split()))
    array.append([x, y])

array.sort()

for i in range(len(array)):
    print(array[i][0], array[i][1])