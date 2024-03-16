n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
left, right = 0, 0
result = 2000000000
while right < n:
    diff = nums[right] - nums[left]
    if diff < m:
        right += 1
    elif diff > m:
        result = min(result, diff)
        left += 1
    else:
        result = m
        break
print(result)