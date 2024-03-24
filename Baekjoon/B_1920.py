n = int(input())
a = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
a.sort()

for num in nums:
    left, right = 0, n - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if num == a[mid]:
            print(1)
            flag = True
            break
        elif num > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if not flag:
        print(0)