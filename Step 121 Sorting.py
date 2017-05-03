n = int(input())
numbers = [int(x) for x in input().split()]
pairs = list(zip(numbers, range(n)))
pairs.sort(key=lambda item: item[0])
indexes = [item[1] + 1 for item in pairs]
print(*indexes)
