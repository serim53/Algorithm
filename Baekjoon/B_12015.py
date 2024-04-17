def binary_search(num):
    start, end = 0, len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start


n = int(input())
a = list(map(int, input().split()))
arr = [0]
for i in range(n):
    if arr[-1] < a[i]:
        arr.append(a[i])
    elif arr[-1] > a[i]:
        idx = binary_search(a[i])
        arr[idx] = a[i]

print(len(arr) - 1)