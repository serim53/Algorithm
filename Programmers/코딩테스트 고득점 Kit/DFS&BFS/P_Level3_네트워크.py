def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if not visited[com]:
            DFS(n, computers, com, visited)
            answer += 1
    return answer


def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if not visited[connect]:
                DFS(n, computers, connect, visited)
