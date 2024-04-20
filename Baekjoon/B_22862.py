def find_largest_arr(start):
    global odd, end, temp, result
    while odd <= k and end < n:
        if nums[end] % 2:
            odd += 1
        else:
            temp += 1
        end += 1

        if start == 0 and end == n:
            result = temp
            return
    if odd == k + 1:
        result = max(temp, result)
    if nums[start] % 2:
        odd -= 1
    else:
        temp -= 1

n, k = map(int, input().split())
nums = list(map(int, input().split()))
end = 0
result = 0
temp = 0
odd = 0

for start in range(n):
    find_largest_arr(start)

print(result)