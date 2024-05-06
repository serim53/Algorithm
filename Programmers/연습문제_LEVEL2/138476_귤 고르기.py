from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    dict = defaultdict(int)
    for t in tangerine:
        dict[t] += 1
    nums = sorted(dict.items(), key=lambda x: -x[1])
    temp = k
    for n in nums:
        if temp <= 0:
            break
        temp -= n[1]
        answer += 1
    return answer