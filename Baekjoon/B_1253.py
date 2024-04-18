import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(n):
    start, end = 0, n - 1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        if arr[start] + arr[end] < arr[i]:
            start += 1
        elif arr[start] + arr[end] > arr[i]:
            end -= 1
        else:
            result += 1
            break
print(result)