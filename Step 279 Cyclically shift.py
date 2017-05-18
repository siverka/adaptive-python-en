n = int(input())
numbers = [int(x) for x in input().split()]
m = 1
shifted = numbers[n-m:] + numbers[:n-m]
print(*shifted)
