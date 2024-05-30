def solution(keymap, targets):
    answer = []
    dict = {}
    for str in keymap:
        for i in range(len(str)):
            st = str[i]
            if st in dict.keys():
                if dict[st] > i + 1:
                    dict[st] = i + 1
            else:
                dict[st] = i + 1

    for word in targets:
        flag = False
        cnt = 0
        for str in word:
            if str not in dict.keys():
                flag = True
                break
            else:
                cnt += dict[str]
        if flag:
            answer.append(-1)
        else:
            answer.append(cnt)
    return answer