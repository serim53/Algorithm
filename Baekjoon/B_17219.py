import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for _ in range(n):
    address, passwd = input().split()
    dict[address] = passwd
for _ in range(m):
    site = input().rstrip()
    print(dict[site])