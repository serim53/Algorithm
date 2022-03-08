from itertools import combinations
n = int(input())
nums = [i for i in range(n)]
result = 1e9
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

for start in combinations(nums, n//2):
    link = list(set(nums) - set(start))
    startSum, linkSum = 0, 0
    for numStart in combinations(start, 2):
        startSum += s[numStart[0]][numStart[1]]
        startSum += s[numStart[1]][numStart[0]]
    for numLink in combinations(link, 2):
        linkSum += s[numLink[0]][numLink[1]]
        linkSum += s[numLink[1]][numLink[0]]
    result = min(result, abs(startSum - linkSum))

print(result)