# 이모티콘은 10, 20, 30, 40 중 하나로 설정
# users([[비율, 가격]])의 길이 100 이하, emotions의 길이 7 이하
# 1. 이모티콘 플러스 가입자를 늘리는 것
# 2. 이모티콘 판매액을 높이는 것
# 각 유저의 기준 비율보다 낮으면서도 가격은 높아야 함

from itertools import product

def solution(users, emoticons):
    len_emo = len(emoticons)
    subscribers, sales = 0, 0
    for permu in product([10, 20, 30, 40], repeat=len_emo):
        temp_sub, temp_sales = 0, 0
        permu = list(permu)
        for user in users:
            total_cost = 0 
            ratio, cost = user
            for i in range(len(permu)):
                if permu[i] >= ratio:
                    total_cost += int(emoticons[i] * (100 - permu[i]) * 0.01)
                if cost <= total_cost:
                    temp_sub += 1
                    break
            if cost > total_cost:
                temp_sales += total_cost
        if subscribers < temp_sub:
            subscribers, sales = temp_sub, temp_sales
        elif subscribers == temp_sub:
            if sales < temp_sales:
                sales = temp_sales
                p = permu
    return [subscribers, sales]

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
