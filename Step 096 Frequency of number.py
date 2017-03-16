n = int(input())
numbers = input().split()
counts = {i: 0 for i in set(numbers)}

for number in numbers:
    counts[number] += 1

print(1 if max(counts.values()) > n / 2 else 0)
