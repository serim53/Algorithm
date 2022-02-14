def solution(clothes):
    answer = 1
    dict = {}
    for i in clothes:
        if i[1] not in dict.keys():
            dict[i[1]] = 1
        else:
            dict[i[1]] += 1
    for i in dict.values():
        answer *= i + 1
    answer -= 1
    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))