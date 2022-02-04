def solution(numbers, target):
    answer = 0
    stack = []
    length = len(numbers)
    stack.append([-numbers[0], 0])
    stack.append([numbers[0], 0])

    while stack:
        num, i = stack.pop()
        if i + 1 == length:
            if num == target:
                answer += 1
        else:
            stack.append([num - numbers[i + 1], i + 1])
            stack.append([num + numbers[i + 1], i + 1])

    return answer


print(solution([1, 1, 1, 1, 1], 3))
