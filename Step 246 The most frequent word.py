from operator import itemgetter

words = []
with open('input_step_246.txt', 'r') as file:
    for line in file:
        words.extend([w.lower() for w in line.split()])

set_words = list(set(words))
counts = [words.count(w) for w in set_words]
d = list(zip(set_words, counts))
d = sorted(sorted(d, key=itemgetter(0)), key=itemgetter(1), reverse=True)
print(*d[0])
