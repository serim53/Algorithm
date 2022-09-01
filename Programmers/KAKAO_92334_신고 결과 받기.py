from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    name = defaultdict(set)
    count = defaultdict(int)

    for r in report:
        f, t = r.split()
        name[f].add(t)
        count[t] += 1

    for id in id_list:
        result = 0
        for n in name[id]:
            if count[n] >= k:
                result += 1
        answer.append(result)

    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))