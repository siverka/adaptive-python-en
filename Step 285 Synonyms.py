n = int(input())
d = [input().split() for _ in range(n)]
word = input()
for words in filter(lambda pair: word in pair, d):
    words.remove(word)
    print(*words)
