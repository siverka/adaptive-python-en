from operator import itemgetter

words = [w.lower() for w in input().split()]
# words = []
# with open('file', 'r') as file:
#     for line in file:
#         words.append([w.lower() for w in line.strip()])

set_words = list(set(words))
counts = [words.count(w) for w in set_words]
d = list(zip(set_words, counts))
d.sort(key=itemgetter(1, 0))
print(d)
