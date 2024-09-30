n = int(input())
nums = list(map(int, input().split()))
start, end = 0, n - 1
min_result = abs(nums[start] + nums[end])
result = (start, end)
while start < end:
    sum_nums = nums[start] + nums[end]
    if abs(sum_nums) <= min_result:
        min_result = abs(sum_nums)
        result = (start, end)
        if sum_nums == 0:
            break
    if sum_nums < 0:
        start += 1
    else:
        end -= 1
print(nums[result[0]], nums[result[1]])
