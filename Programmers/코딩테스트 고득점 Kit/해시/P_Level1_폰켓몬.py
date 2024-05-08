def solution(nums):
    dict = {}
    for n in nums:
        if n in dict.keys():
            dict[n] += 1
        else:
            dict[n] = 1
    kinds = len(dict.keys())
    if (len(nums) // 2) > kinds:
        return kinds
    else:
        return len(nums) // 2