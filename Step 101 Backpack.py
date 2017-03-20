capacity, n = map(int, input().split())
weights = [int(w) for w in input().split()]
# capacity, n = 10, 3
# weights = [1, 4, 8]
weights.sort(reverse=True)
# print(weights)
backpack = 0
for w in weights:
    if w + backpack <= capacity:
        backpack += w

print(backpack)
