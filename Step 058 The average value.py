n = int(input())
sequence = []
while n != 0:
    sequence.append(n)
    n = int(input())
print(sum(sequence) / len(sequence))
