n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
sum = 0
for i in arr:
    result += i
    sum += result

print(sum)