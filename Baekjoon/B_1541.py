exp = input().split('-')
nums = []

for i in exp:
    sum_num = 0
    temp = i.split('+')
    for j in temp:
        sum_num += int(j)
    nums.append(sum_num)

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

print(result)