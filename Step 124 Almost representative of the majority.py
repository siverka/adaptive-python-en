n = int(input())
array = input().split()
repeats = {a: 0 for a in set(array)}
for a in array:
    repeats[a] += 1
answer = any(map(lambda r: r > n / 3, repeats.values()))
print(int(answer))
