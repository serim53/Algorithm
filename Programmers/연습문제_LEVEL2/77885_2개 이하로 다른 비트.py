def solution(numbers):
    answer = []
    for number in numbers:
        # 짝수인 경우 마지막 비트가 0이므로 마지막 비트를 1로 변경한 것이 최소.
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        # 홀수인 경우 가장 마지막 0비트의 인덱스를 찾아, 1로 변경하고 그 다음 비트를 0으로 변경해준 것이 최소.
        number_bin = '0' + bin(number)[2:]
        idx = number_bin.rindex('0')
        number_bin = number_bin[:idx] + '10' + number_bin[idx + 2:]
        answer.append(int(number_bin, 2))
    return answer