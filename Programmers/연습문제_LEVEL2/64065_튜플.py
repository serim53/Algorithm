def solution(s):
    answer=[]
    arr = []
    for i in s.split("},"):
        arr.append(i.replace("{","").replace("}","").split(","))
    arr.sort(key=len)
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
    return list(map(int, answer))


solution("{{1,2,3},{2,1},{1,2,4,3},{2}")
