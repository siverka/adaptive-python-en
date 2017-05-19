n, k = map(int, input().split())
numbers = [int(x) for x in input().split()]
shifted = numbers[k % n:] + numbers[:k % n]
print(*shifted)
