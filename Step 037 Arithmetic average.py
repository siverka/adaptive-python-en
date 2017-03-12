a, b = int(input()), int(input())
numbers = [i for i in range(a, b+1) if i % 3 == 0]
print(sum(numbers) / len(numbers))
