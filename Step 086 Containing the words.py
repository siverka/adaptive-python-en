words = input().split()
lengths = list(map(len, words))
d = {l: lengths.count(l) for l in sorted(set(lengths))}
for length, amount in d.items():
    print('%d: %s' % (length, amount))
