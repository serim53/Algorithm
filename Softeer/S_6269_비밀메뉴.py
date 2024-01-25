import sys 
input = sys.stdin.readline
m, n, k = map(int, input().split())
secret_key = list(map(str, input().split()))
user_input = list(map(str, input().split()))
if ''.join(secret_key) in ''.join(user_input):
    print("secret")
else:
    print("normal")
