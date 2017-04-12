d = int(input())
words = []
for _ in range(d):
    words.append(input().lower())

l = int(input())
text = []
for _ in range(l):
    text.extend(w.lower() for w in input().split())

for w in set(text):
    if w not in words:
        print(w)
