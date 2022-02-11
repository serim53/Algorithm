def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights and truck_weights[0] + sum(bridge) <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            if truck_weights:
                bridge.append(0)
    return answer


print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))