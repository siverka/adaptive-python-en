n = int(input())
sequence = []
i = 1
while len(sequence) < n:
    sequence.extend([i] * min(i, n - len(sequence)))
    i += 1
print(*sequence)
