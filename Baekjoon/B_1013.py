# (100+1+ | 01)+
import re

exp = re.compile('(100+1+|01)+')
t = int(input())
for _ in range(t):
    st = input().rstrip()
    if exp.fullmatch(st):
        print("YES")
    else:
        print("NO")
