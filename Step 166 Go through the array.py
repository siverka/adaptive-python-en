m, n = [int(i) for i in input().split()]
numbers = [int(i) for i in input().split()]
counts = [0 for _ in range(n)]
for i in numbers:
    counts[i-1] += 1
print(*counts)

