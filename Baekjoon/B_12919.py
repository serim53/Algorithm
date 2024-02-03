import sys
input = sys.stdin.readline

def dfs(str_t):
    global result
    if str_t == s:
        result = 1
        return
    if len(str_t) == 0:
        return
    if str_t[-1] == 'A':
        dfs(str_t[:-1])
    if str_t[0] == 'B':
        dfs(str_t[1:][::-1])

s = input().strip()
t = input().strip()
result = 0
dfs(t)
print(result)