n, k = map(int, input().split())
arr = list(input())
result = 0

for i in range(len(arr)):
    if arr[i] == 'P':
        for j in range(i - k, i + k + 1):
            if 0 <= j < len(arr) and arr[j] == 'H':
                arr[j] = 'U'
                result += 1
                break
print(result)