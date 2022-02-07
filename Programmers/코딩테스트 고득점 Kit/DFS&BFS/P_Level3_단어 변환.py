from collections import deque

def check(s, begin):
    answer = 0
    for i in range(len(s)):
        if list(s)[i] != list(begin)[i]:
            answer += 1
    return True if answer == 1 else False


def solution(begin, target, words):

    queue = deque()
    queue.append([begin, []])

    if target not in words:
        return 0

    while queue:
        n, l = queue.popleft()
        for word in words:
            if word not in l and check(word, n):
                if word == target:
                    return len(l) + 1
                temp = l[0:]
                temp.append(word)
                queue.append([word, temp])

    return 0