n = int(input())
words = [str(input()) for _ in range(n)]
words = list(set(words))
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)