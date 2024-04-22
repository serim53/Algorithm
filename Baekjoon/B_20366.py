n = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = 1e9
for i in range(n):
    for j in range(i + 3, n):
        start, end = i + 1, j - 1
        while start < end:
            diff = (nums[i] + nums[j]) - (nums[start] + nums[end])
            if abs(result) > abs(diff):
                result = abs(diff)
            if diff < 0:
                end -= 1
            else:
                start += 1
print(result)