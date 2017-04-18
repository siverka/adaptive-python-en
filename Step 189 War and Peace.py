words = [w.lower() for w in input().split()]
count = {w: words.count(w) for w in set(words)}
for item in count.items():
    print(*item)
