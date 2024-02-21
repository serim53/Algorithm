def check(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(str(input().rstrip()))
    nums.sort()
    if check(nums):
        print("YES")
    else:
        print("NO")