m = int(input())
numbers = [int(n) for n in input().split()]
numbers.sort()
print(numbers[-1] * numbers[-2])
