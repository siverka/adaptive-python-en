numbers = [int(x) for x in input().split()]
n = len(numbers)
diffs = [abs(numbers[i+1] - numbers[i]) for i in range(n-1)]
diffs.sort()
jolly = diffs == list(range(1, n))
print('Jolly' if jolly else 'Not jolly')
