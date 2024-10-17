from collections import defaultdict

def solution(weights):
    answer = 0
    dict = defaultdict(int)
    weights.sort()
    for weight in weights:
        if dict[weight]:
            answer += dict[weight]
        # 동일 무게 착석
        dict[weight] += 1
        # 4 - 2 착석
        dict[weight * 2] += 1
        # 3 - 2 착석
        if weight % 2 == 0:
            dict[(weight // 2) * 3] += 1
        # 4 - 3 착석
        if weight % 3 == 0:
            dict[(weight // 3) * 4] += 1
    return answer
