def solution(tickets):

    routes = dict()
    for i in tickets:
        if i[0] in routes:
            routes[i[0]].append(i[1])
        else:
            routes[i[0]] = [i[1]]

    for i in routes.keys():
        routes[i].sort(reverse = True)

    answer = []
    start = ["ICN"]

    while start:
        target = start[-1]
        if target not in routes or len(routes[target]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[target].pop())

    return answer[::-1]