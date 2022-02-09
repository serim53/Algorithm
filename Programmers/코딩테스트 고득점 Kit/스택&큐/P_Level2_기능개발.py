from collections import deque
import math

def solution(progresses, speeds):

    answer = []
    num = 1
    queue = deque()

    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))

    big = queue.popleft()
    while queue:
        now = queue.popleft()
        if big >= now:
            num += 1
        else:
            answer.append(num)
            num = 1
            big = now

    answer.append(num)

    return answer
