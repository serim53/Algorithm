import math

def solution(fees, records):
    bt, bf, ut, uf = fees
    answer = {}
    temp = []
    result = []
    for r in records:
        # 시간을 :로 분리
        time = r.split()[0].split(":")
        # 시간을 분 단위로 변형
        minutes = int(time[0]) * 60 + int(time[1])
        if r.split()[2] == "IN":
            temp.append([minutes, r.split()[1]])
        else:
            for t in temp:
                if t[1] == r.split()[1]:
                    times = minutes - t[0]
                    if t[1] in answer:
                        answer[t[1]] += times
                    else:
                        answer[t[1]] = times
                    temp.remove(t)
    for t2 in temp:
        times = 1439 - t2[0]
        if t2[1] in answer:
            answer[t2[1]] += times
        else:
            answer[t2[1]] = times

    answer = sorted(answer.items())

    for a in answer:
        fee = bf + uf * math.ceil((a[1] - bt if a[1] - bt > 0 else 0) / ut)
        result.append(fee)
    return result

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))