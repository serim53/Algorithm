import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    array.append((age, name))

array.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in array:
    print(i[0], i[1])