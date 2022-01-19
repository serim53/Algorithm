import sys

input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()
for i in range(len(array)):
    print(array[i], end='\n')