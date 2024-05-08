from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for permu in permutations(dungeons, len(dungeons)):
        power = k
        nums = 0
        for p in permu:
            if power < p[0]:
                break
            power -= p[1]
            nums += 1
        if nums > answer:
            answer = nums
    return answer