from collections import Counter

def solution(topping):
    answer = 0
    cs = Counter(topping)
    bro = {}
    for i in range(len(topping)):
        if topping[i] in bro:
            bro[topping[i]] += 1
        else:
            bro[topping[i]] = 1
        cs[topping[i]] -= 1
        if not cs[topping[i]]:
            del(cs[topping[i]])
        if len(cs) == len(bro):
            answer += 1
    return answer