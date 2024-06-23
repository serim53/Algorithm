def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])

    stack = []
    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break

        subject, time, dur = plans[i]
        n_subject, n_time, n_dur = plans[i + 1]
        if time + dur <= n_time:
            answer.append(subject)
            temp = n_time - (time + dur)

            while temp != 0 and stack:
                s, t, d = stack.pop()
                if temp >= d:
                    answer.append(s)
                    temp -= d
                else:
                    stack.append([s, t, d - temp])
                    temp = 0
        else:
            plans[i][2] = dur - (n_time - time)
            stack.append(plans[i])

    while stack:
        subject, _, _ = stack.pop()
        answer.append(subject)

    return answer
