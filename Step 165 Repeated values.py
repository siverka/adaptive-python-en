numbers = [int(n) for n in input().split()]
counts = {n: numbers.count(n) for n in numbers}
print(*[key for key in counts.keys() if counts[key] > 1])
