sequence = [int(input())]
while sum(sequence) != 0:
    sequence.append(int(input()))
print(sum(i ** 2 for i in sequence))
