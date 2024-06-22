def solution(bandage, health, attacks):
    max_health = health
    time = 0
    continue_time = 0

    dict = {}
    for attack in attacks:
        dict[attack[0]] = attack[1]

    while time <= attacks[-1][0]:

        if time in dict:
            health -= dict[time]
            continue_time=0
            if health <= 0:
                return -1
        else:
            continue_time += 1
            if continue_time < bandage[0]:
                health += bandage[1]
                if health > max_health:
                    health = max_health
            else:
                health = health + bandage[1] + bandage[2]
                if health > max_health:
                    health = max_health
                continue_time=0
        time+=1

    return health