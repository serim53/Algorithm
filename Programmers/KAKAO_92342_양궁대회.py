from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_val = -1e9
    min_sum = 1e9
    scores = list(combinations_with_replacement(range(0, 11), n))
    for score in scores:
        sum_score = 0
        apeach, lion = 0, 0
        info_lion = [0] * 11
        for s in score:
            info_lion[10 - s] += 1
        for i in range(11):
            sum_score += info_lion[i] * (10 - i)
            if info[i] == 0 and info_lion[i] == 0:
                continue
            elif info[i] >= info_lion[i]:
                apeach += (10 - i)
            else:
                lion += (10 - i)
        if lion > apeach:
            diff = lion - apeach
            if (diff == max_val and min_sum > sum_score) or (diff > max_val):
                max_val = diff
                min_sum = sum_score
                answer = info_lion
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))