n = int(input())
a = list(map(int, input().split()))
left, right = 0, n - 1
result = a[left] + a[right]
while left < right:
    temp = a[left] + a[right]
    if abs(result) > abs(temp):
        result = temp
    if temp < 0:
        left += 1
    else:
        right -= 1
print(result)