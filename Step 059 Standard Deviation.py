from statistics import stdev

sequence = []
n = int(input())
while n != 0:
    sequence.append(n)
    n = int(input())
print(stdev(sequence))

