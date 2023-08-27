t = int(input())
for _ in range(t):
    tc_list = list(input())
    score = 0
    sum_score = 0
    for tc in tc_list:
        if tc == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)