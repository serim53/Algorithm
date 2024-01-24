import sys

def check(nums):
    if nums[0] == 1:
        for i in range(1, 8):
            if nums[i] != asc[i]:
                return "mixed"
        return "ascending"
    elif nums[0] == 8:
        for i in range(1, 8):
            if nums[i] != des[i]:
                return "mixed"
        return "descending"
    else:
        return "mixed"

asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]
nums = list(map(int, sys.stdin.readline().split()))
print(check(nums))
