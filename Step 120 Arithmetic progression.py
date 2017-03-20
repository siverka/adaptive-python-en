sequence = [int(i) for i in input().split()]
if len(sequence) == 1:
    print('Yes')
else:
    sequence.sort()
    diff = [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]
    print('Yes' if len(set(diff)) == 1 else 'No')
