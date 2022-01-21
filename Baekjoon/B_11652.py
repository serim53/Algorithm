import sys
input = sys.stdin.readline

n = int(input())
cards = {}

for i in range(n):
    card = int(input())
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

result = sorted(cards.items(), key = lambda x: (-x[1], x[0]))
print(result[0][0])